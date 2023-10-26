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

    



[1] https://data.world/brentbrewington/atlanta-city-employee-salaries 
