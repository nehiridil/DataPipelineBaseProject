Data Pipeline Base Project
This project aims to create a summary report of the "Atlanta City Employee Salaries" dataset using a preferable database and data orchestration tool.

🌟 Features
Database: Google BigQuery

Seamlessly pull and process data with Google's BigQuery.
Orchestration Tool: Apache Airflow

Efficient data pipeline management and scheduling with Apache Airflow.
BigQuery
BigQuery is a serverless, highly scalable, and cost-effective multi-cloud data warehouse.

Setup
Create a new project in Google Cloud Console and navigate to BigQuery.

Create a dataset called 'salaries'.

Use the dataset provided here to create a table named 'atlanta_salaries_report'.

setup-image

Data Processing
Using 'atlanta_salaries_report', create 'atlanta_salaries_report_filtered'. Include entries with the 0.95 percentile in annual salary and exclude those where 'Organization' includes 'Atlanta'.

filter-image

Using 'atlanta_salaries_report_filtered', create 'atlanta_salaries_report_filtered_summary'. This will show the average salaries of women and men across different ages.

summary-image

Python Scripts and BigQuery Authentication
Install the bigquery library: pip install google-cloud-bigquery
Ensure the installation path for google-cloud-bigquery is on your PYTHONPATH. If not, add it.
Windows: pip show google-cloud-bigquery | findstr Location
Following the above steps might lead to a 'google.auth.exceptions.DefaultCredentialsError'. To resolve this:

Set up Google Cloud SDK.

Create a service account from IAM&Admin Console and assign the provided roles.

iam-image

Finalize authentication using:

scss
Copy code
gcloud auth application-default login --impersonate-service-account <service_account_mail_address>
Airflow
Install Docker Desktop to host Airflow on your local machine.

Using the base airflow image, create a docker container.

Update docker-compose.yml with your Google Service Account key path:

bash
Copy code
<path_to_your_service_account_key>/my-key.json:/opt/airflow/my-key.json
Start Airflow:

Copy code
docker-compose build
docker-compose up
You can access Airflow UI at localhost:8080.

DAGS
Under the Airflow directory in the Dags folder, define your dags. This project includes one dag with two tasks: one for filtering and another for creating the summary table.

dags-image

Exception Handling and Logs
For simplicity, only the "table not found" exception is tested. If it occurs, it's visible in the logs and the job fails:

yaml
Copy code
[2023-10-27, 08:32:38 UTC] {utils.py:16} ERROR - An unexpected error occurred: 404 Not found: Table parcellab-task:salaries.atlanta_salaries_report_wrong_table was not found in location US
Location: US
Job ID: 9b586e96-b0bb-4015-b8f1-3b656e437a28
