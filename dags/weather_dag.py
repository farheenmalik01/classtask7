from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import os

# Define your functions (tasks)
def collect_data():
    os.system("python D:/classTask7/weather_data_pipeline/app.py")
    print("Data collection complete.")

def preprocess_data():
    os.system("python D:/classTask7/weather_data_pipeline/preprocess.py")
    print("Data preprocessing complete.")

# Default arguments for the tasks
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Create the DAG object
with DAG('weather_pipeline',
         default_args=default_args,
         description='Weather Data Pipeline',
         schedule_interval='@daily',
         start_date=datetime(2024, 1, 1),
         catchup=False) as dag:

    task1 = PythonOperator(
        task_id='app',
        python_callable=collect_data
    )

    task2 = PythonOperator(
        task_id='preprocess',
        python_callable=preprocess_data
    )

    # Set task dependencies
    task1 >> task2
