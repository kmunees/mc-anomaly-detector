import os
import psycopg2
from logger_configuration import logger

#Get logger
logger = logger()

def chunk_log_content(content: str):
    chunks = content.splitlines()
    return [chunk for chunk in chunks if chunk.strip()]

def insert_processed_file(new_file):
    db_config = {
        'dbname': 'airflow',
        'user': 'airflow',
        'password': 'airflow',
        'host': '192.168.29.111',
        'port': 5432
    }
    try:
        with psycopg2.connect(**db_config) as conn:
            with conn.cursor() as cursor:
                # Insert the new processed file
                cursor.execute("INSERT INTO public.mc_files (processed_files) VALUES (%s)", (new_file,))
                print("Processed file updated successfully.")
    except psycopg2.Error as e:
        print(f"Database error: {e}")

def is_file_processed(file_path):
    db_config = {
        'dbname': 'airflow',
        'user': 'airflow',
        'password': 'airflow',
        'host': '192.168.29.111',
        'port': 5432
    }
    try:
        with psycopg2.connect(**db_config) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT 1 FROM public.mc_files WHERE processed_files = %s", (file_path,))
                result = cursor.fetchone()
                return result is not None
    except psycopg2.Error as e:
        print(f"Database error: {e}")
        return False

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
                    insert_processed_file(file_path)
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


