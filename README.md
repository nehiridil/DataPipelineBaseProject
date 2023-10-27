# Data Pipeline Base Project

This project aims to create a summary report of the "Atlanta City Employee Salaries" dataset using a preferable database and data orchestration tool.

## 🌟 Features

- **Database**: Google BigQuery
  - Seamlessly pull and process data with Google's BigQuery.

- **Orchestration Tool**: Apache Airflow 
  - Efficient data pipeline management and scheduling with Apache Airflow.

## BigQuery

BigQuery is a serverless, highly scalable, and cost-effective multi-cloud data warehouse.

### Setup

1. Create a new project in Google Cloud Console and navigate to BigQuery.
2. Create a dataset called 'salaries'.
3. Use the dataset provided [here](https://data.world/brentbrewington/atlanta-city-employee-salaries) to create a table named 'atlanta_salaries_report'.

![setup-image](https://github.com/nehiridil/DataPipelineBaseProject/assets/46990153/6e648845-560c-4895-b8cb-82483c10c53b)

### Data Processing

- Using 'atlanta_salaries_report', create 'atlanta_salaries_report_filtered'. Include entries with the 0.95 percentile in annual salary and exclude those where 'Organization' includes 'Atlanta'.

![filter-image](https://github.com/nehiridil/DataPipelineBaseProject/assets/46990153/9bb14238-1f1d-4a3a-8390-85cb3c1b748b)

- Using 'atlanta_salaries_report_filtered', create 'atlanta_salaries_report_filtered_summary'. This will show the average salaries of women and men across different ages.

![summary-image](https://github.com/nehiridil/DataPipelineBaseProject/assets/46990153/4d2cac2a-81a0-4362-ae6f-b2ac0921b90f)

### Python Scripts and BigQuery Authentication

1. Install the bigquery library:
   ```
   pip install google-cloud-bigquery
   ```
2. Ensure that the path where google-cloud-bigquery is installed is on your PYTHONPATH. If not, add to PYTHONPATH. You can find the installation path with this command in Windows systems:
   ```
   pip show google-cloud-bigquery | findstr Location
   ```
3. After these steps if you try to run the code you will end up with `google.auth.exceptions.DefaultCredentialsError`
     To be able to resolve this issue, 
      - Set up Google Cloud SDK using official setup steps[2]
      - Create a service account from IAM&Admin Console and assign them given roles,
      ![image](https://github.com/nehiridil/DataPipelineBaseProject/assets/46990153/81f83a81-7c15-4eb6-af0f-4b3dcf37b026)
      - Then, run this command to finalize authentication:
       ```
        gcloud auth application-default login --impersonate-service-account <service_account_mail_address>
       ```

### Airflow
  To be able to host airflow on your local machine, you need to install Docker Desktop first.
  Then, using the base airflow image, create a docker container and complete configurations in the `docker-compose.yml`. You need to change this part with your Google Service Account key path in docker-compose-yml:
  ```
   <path_to_your_service_account_key>/my-key.json:/opt/airflow/my-key.json
  ```
  After running the above commands, you will be able to reach Airflow UI from `localhost:8080`
  ```
   docker-compose build
   docker-compose up
  ```
### DAGS
  Under the Airflow directory in the 'Dags' folder, you need to define dags. In this project, one dag with two tasks was created. One task will run the filtering function and another will run the creation of summary table.
  ![image](https://github.com/nehiridil/DataPipelineBaseProject/assets/46990153/79ef4213-bc3d-4bf8-bf22-615b94b85227)
  - Exception Handling and Logs
  For the simplicity table not found exception is tested, when it occurs it can be seen in the logs and job fails.
  ```
  [2023-10-27, 08:32:38 UTC] {utils.py:16} ERROR - An unexpected error occurred: 404 Not found: Table parcellab-task:salaries.atlanta_salaries_report_wrong_table was not found in location US
  Location: US
  Job ID: 9b586e96-b0bb-4015-b8f1-3b656e437a28
  ```
    

      

    



[1] https://data.world/brentbrewington/atlanta-city-employee-salaries 
[2] https://cloud.google.com/sdk/docs/install
