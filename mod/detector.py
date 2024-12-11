import os
import json
from pathlib import Path
import sys
from mod.pg_client import get_patterns_from_db
from mod.ts_influx_client import send_signals_timeseries_db

sys.path.append(str(Path(__file__).parent.absolute()))
from mod.fuzzywuzzy import fuzz

from mod.log_file_reader import LogFileListener


from mod.logger_configuration import logger
from mod.env_loader import get_logfile_path

#Get logger
logger = logger()


def detect():

    file_path = get_logfile_path()
    folder_to_watch = os.path.abspath(file_path)

    logger.info(folder_to_watch)

    if not os.path.isdir(folder_to_watch):
        logger.info(f"Error: The directory {folder_to_watch} does not exist.")
    else:
        logger.info(f"Monitoring folder: {folder_to_watch}")
        log_file_handler = LogFileListener(folder_to_watch)
        logs = log_file_handler.read_logs_from_files()
        if not logs:
            return
        patterns = get_patterns_from_db()
        matched_logs = []

        for log in logs:
            for pattern in patterns:
                pattern_expression = pattern["pattern_expression"]
                if fuzz.partial_ratio(pattern_expression, log) > 80:
                    matched_logs.append({
                        "log": log,
                        "matched_expression": pattern_expression,
                        "log_type": pattern["log_type"],
                        "category": pattern["category"],
                        "severity": pattern["severity"]
                    })
                    break
        logger.info(
            f"The following logs have been identified as anomalies based on matching patterns:\n{json.dumps(matched_logs, indent=4)}")
        if matched_logs:
            logger.info(f"Size of patch content {len(matched_logs)}")
            send_signals_timeseries_db(matched_logs)
            logger.info("Anomalous logs have been successfully persisted to the database.")
        else:
            logger.error("No matched logs available to send to the signals API.")

# def get_patters():
#     file_path = get_pattern_file_path()
#     folder_to_watch = os.path.abspath(file_path)
#     with open(folder_to_watch, 'r') as file:
#      return json.load(file)
