import logging
from utils import utils
from google.cloud import bigquery
client = bigquery.Client(project='parcellab-task')
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_summary_table(table_name):
    client.delete_table(table_name,not_found_ok=True)
    
    summary_query = f'''
    CREATE TABLE IF NOT EXISTS {table_name} AS
        SELECT
        age,
        AVG(CASE WHEN sex = 'Female' THEN annual_salary ELSE NULL END) AS female_average_salary,
        AVG(CASE WHEN sex = 'Male' THEN annual_salary ELSE NULL END) AS male_average_salary
    FROM salaries.atlanta_salaries_report_filtered
    GROUP BY age
  '''

    query_job = client.query(summary_query)
    utils.check_exception(query_job)


def run_summary():
    try:
        logger.info("Summary table creation has started.")
        create_summary_table(
            'salaries.atlanta_salaries_report_filtered_summary')
        logger.info("Summary table creation has finished.")
    except Exception as e:
        logger.error(
            f"ERROR: There was an error during the summary step. Details: {e}")
        raise


if __name__ == "__main__":
    run_summary()
