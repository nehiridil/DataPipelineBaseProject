from google.cloud import bigquery
client = bigquery.Client(project='parcellab-task')


def create_filtered_table(table_name):
    filter_query = f'''
  CREATE TABLE IF NOT EXISTS {table_name} AS
  WITH percentile_95 AS(
    SELECT
      PERCENTILE_CONT(annual_salary,0.95) OVER () AS percentile_salary --84300.01
    FROM
      salaries.atlanta_salaries_report
  )
  SELECT
    t1.*
  FROM salaries.atlanta_salaries_report t1
  LEFT JOIN percentile_95 t2
  ON 1=1
  WHERE 
    t1.annual_salary >= t2.percentile_salary
    AND t1.organization NOT LIKE '%Atlanta%';
  '''

    client.query(filter_query)


def run_filtering():
    print("Filter table create is started.")
    create_filtered_table('salaries.atlanta_salaries_report_filtered')
    print("Filter table create is finished.")


if __name__ == "__main__":
    run_filtering()
