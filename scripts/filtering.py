import logging
from utils import utils
from google.cloud import bigquery
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


client = bigquery.Client(project='parcellab-task')


def create_filtered_table(table_name):
    client.delete_table(table_name,not_found_ok=True)
    
    filter_query = f'''
    CREATE TABLE IF NOT EXISTS {table_name} AS
    WITH percentile_95 AS(
      SELECT DISTINCT
        PERCENTILE_CONT(annual_salary,0.95) OVER () AS percentile_salary --84300.01
      FROM
        salaries.atlanta_salaries_report
    )
    SELECT
      t1.*
    FROM salaries.atlanta_salaries_report t1
    CROSS JOIN percentile_95 t2
    WHERE 
      t1.annual_salary >= t2.percentile_salary
      AND t1.organization NOT LIKE '%Atlanta%';
    '''
    
    query_job = client.query(filter_query)
    utils.check_exception(query_job)


def run_filtering():
    try:
        logger.info("Filter table creation has started.")
        create_filtered_table('salaries.atlanta_salaries_report_filtered')
        logger.info("Filter table creation has finished.")
    except Exception as e:
        logger.error(
            f"ERROR: There was an error during the filtering step. Details: {e}")
        raise


if __name__ == "__main__":
    run_filtering()
