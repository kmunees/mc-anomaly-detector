from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from pathlib import Path
import sys
from mod.logger_configuration import logger
from mod.detector import detect

logger = logger()
sys.path.append(str(Path(__file__).parent.absolute()))

# Define a Python function for the task
def detect_anomaly():
    detect()

def message():
    logger.info("Processing the patch is completed successfully")

# Default arguments for the DAG

# Define the DAG
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=10),
}

with DAG(
    'anomaly_detector_dag',
    default_args=default_args,
    description='A simple example DAG',
    schedule_interval='*/2 * * * *',
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    task1 = PythonOperator(
        task_id='detect_anomaly',
        python_callable=detect_anomaly,
    )

    task2 = PythonOperator(
        task_id='persist_to_db',
        python_callable=message,
    )

    task1 >> task2
