import logging

from google.cloud import bigquery
from google.cloud.bigquery import dbapi

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def check_exception(query_job):
    try:
        query_job.result()
    except dbapi.DatabaseError as db_err:
        logger.error(f"Database error: {db_err}")
        raise
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        raise