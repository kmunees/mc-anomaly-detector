from urllib.parse import quote
import base64
import requests
from mod.logger_configuration import logger
from mod.env_loader import get_ts_influx_token, get_ts_influx_url

logger = logger()

def send_signals_timeseries_db(matched_logs):
    url = get_ts_influx_url()
    headers = {
        "Authorization": f"Token {get_ts_influx_token()}",
        "Content-Type": "text/plain"
    }

    # Build the body dynamically for batch data
    body = "\n".join(
        f"signals_api,"
        f"matched_expression={quote(log['matched_expression'])},"
        f"log_type={quote(log['log_type'])},"
        f"category={quote(log['category'])},"
        f"severity={quote(log['severity'])} "
        f"value=\"{encode_base64(log['log'])}\""
        for log in matched_logs
    )

    # Log and send the request
    logger.info(f"Persisting batch to timeseries DataBase:\n{body}")
    try:
        response = requests.post(url, headers=headers, data=body)
        response.raise_for_status()
        logger.info(f"API Response: {response.status_code} {response.text}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to persist batch data to API: {e}")


def encode_base64(value):
    encoded = base64.b64encode(value.encode('utf-8')).decode('utf-8')
    return quote(encoded)