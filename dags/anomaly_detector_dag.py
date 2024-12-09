from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
# from detector.detector import detect


# Define a Python function for the task
def detect_anomaly():
    # detect()
    print("Anomalous logs have been detected")


def message():
    print("Anomalous logs have been successfully persisted to the database.")

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    'anomaly_detector_dag',
    default_args=default_args,
    description='A simple example DAG',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 12, 6),
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
