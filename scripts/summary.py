from google.cloud import bigquery
client = bigquery.Client(project='parcellab-task')


def create_summary_table(table_name):
    summary_query = f'''
    CREATE TABLE IF NOT EXISTS {table_name} AS
    SELECT
    age,
    AVG(CASE WHEN sex = 'Female' THEN annual_salary ELSE NULL END) AS female_average_salary,
    AVG(CASE WHEN sex = 'Male' THEN annual_salary ELSE NULL END) AS male_average_salary
    FROM salaries.atlanta_salaries_report_filtered
    GROUP BY age
  '''

    client.query(summary_query)


def run_summary():
    print("Summary table create is started.")
    create_summary_table('salaries.atlanta_salaries_report_filtered_summary')
    print("Summary table create is finished.")


if __name__ == "__main__":
    run_summary()
