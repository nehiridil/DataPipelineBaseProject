from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import sys

# Append the directory to sys.path
sys.path.append("/opt/airflow")

from scripts.filtering import run_filtering
from scripts.summary import run_summary

default_args = {
    'owner': 'Idil Yuksel',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 5,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'salary_summary_dag',
    default_args=default_args,
    description='Filters salary table and summarizes it',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 10, 25),
    catchup=True,
)

run_filtering_task = PythonOperator(
    task_id='run_filtering',
    python_callable=run_filtering,
    dag=dag,
)

run_summary_task = PythonOperator(
    task_id='run_summary',
    python_callable=run_summary,
    dag=dag,
)

run_filtering_task >> run_summary_task
