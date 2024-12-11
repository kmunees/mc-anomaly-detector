import os
from logger_configuration import logger
from mod.pg_client import is_file_processed, insert_processed_file_path

#Get logger
logger = logger()

def chunk_log_content(content: str):
    chunks = content.splitlines()
    return [chunk for chunk in chunks if chunk.strip()]

class LogFileListener:
    def __init__(self, folder_to_watch):
        self.folder_to_watch = folder_to_watch

    def read_logs_from_files(self):

        # List all .log files in the directory
        logger.info(f"All log files in folder {os.listdir(self.folder_to_watch)}")

        # List to collect chunks from all files
        all_chunks = []

        for filename in os.listdir(self.folder_to_watch):
            file_path = os.path.join(self.folder_to_watch, filename)

            if os.path.isfile(file_path) and filename.endswith('.log'):

                if not is_file_processed(file_path):
                    # Insert the new file path into the database
                    insert_processed_file_path(file_path)
                    logger.info(f"New log file detected: {file_path}")
                    try:
                        with open(file_path, 'r') as file:
                            content = file.read()
                            chunks = chunk_log_content(content)
                            all_chunks.extend(chunks)  # Add chunks to the list
                    except Exception as e:
                        logger.error(f"Error reading file {file_path}: {e}")
                else:
                    logger.info(f"Log file already processed: {file_path}")

        # Return all chunks after processing all files
        return all_chunks if all_chunks else None


