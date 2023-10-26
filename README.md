# Data Pipeline Base Project
This project aims to create a summary report of the "Atlanta City Employee Salaries"[1] dataset using a preferable database and data orchestration tool.

🌟 Features
Database - Google BigQuery
  *Seamlessly pull and process data with Google's BigQuery.
Orchestration Tool - Apache Airflow 
  *Efficient data pipeline management and scheduling with Apache Airflow.

BigQuery
  BigQuery is a serverless, highly scalable, and cost-effective multi-cloud data warehouse.

  Setup
    - Create a new project in Google Cloud Console and navigate to BigQuery.
    - Create a dataset called 'salaries' and a table using the dataset[1] provided and name as 'atlanta_salaries_report'.
    ![image](https://github.com/nehiridil/DataPipelineBaseProject/assets/46990153/6e648845-560c-4895-b8cb-82483c10c53b)

  Data Processing
    - Using 'atlanta_salaries_report', create 'atlanta_salaries_report_filtered' by including entries with 0.95 percentile in annual salary and exclude who has 'Organization' includes 'Atlanta'. Preview of the table,
     ![image](https://github.com/nehiridil/DataPipelineBaseProject/assets/46990153/9bb14238-1f1d-4a3a-8390-85cb3c1b748b)
    - Using 'atlanta_salaries_report_filtered', create 'atlanta_salaries_report_filtered_summary' to be able to show the average salaries of women and men of different ages. Preview of the table,
    ![image](https://github.com/nehiridil/DataPipelineBaseProject/assets/46990153/4d2cac2a-81a0-4362-ae6f-b2ac0921b90f)

   Python Scripts and BigQuery Authentication
    - To be able to run queries inside a Python Script, these steps should be followed,
      - Install the bigquery library -> pip install google-cloud-bigquery
      - Ensure that the path where google-cloud-bigquery is installed is on your PYTHONPATH. If not, add to PYTHONPATH. You can find the installation path with this command in Windows systems-> pip show google-cloud-bigquery | findstr Location
     After these steps if you try to run the code you will end up with 'google.auth.exceptions.DefaultCredentialsError'
     To be able to resolve this issue, 
      - Set up Google Cloud SDK using official setup steps[2]
      - Create a service account from IAM&Admin Console and assign them given roles,
      ![image](https://github.com/nehiridil/DataPipelineBaseProject/assets/46990153/81f83a81-7c15-4eb6-af0f-4b3dcf37b026)
      - Then, run this command to finalize authentication:
       gcloud auth application-default login --impersonate-service-account <service_account_mail_address>

Airflow

      

    



[1] https://data.world/brentbrewington/atlanta-city-employee-salaries 
[2] https://cloud.google.com/sdk/docs/install
