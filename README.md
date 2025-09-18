# Movie-Data-Pipeline
An end to end data pipeline on AWS for movie data analysis, demonstrating skills in data ingestion, transformation, and cloud storage.
# Movie Data Analysis Pipeline
# Movie Data Analysis Pipeline

This project is an end-to-end data pipeline that processes raw movie data, demonstrating my skills in data ingestion, transformation, and cloud storage.

## **Project Goal**

To showcase a practical, hands-on example of a data engineering pipeline. This project takes raw, messy data, cleans it using Python, and prepares it for analysis.

## **Pipeline Overview**

The data pipeline follows a simple, three-stage process:

1.  **Ingestion:** Raw movie data is loaded from an **AWS S3 bucket**. This shows how I handle large datasets outside of a code repository.
2.  **Transformation:** A Python script (transform_data.py) cleans the data by handling missing values and converting data types. The script uses the **boto3** library to connect to the S3 bucket.
3.  **Storage:** The cleaned data is saved to a new CSV file within the S3 bucket, ready for further analysis.

## **Technologies & Skills Demonstrated**

* **Python:** Used to write the data transformation logic.
* **AWS S3:** Utilized as a scalable, cloud-based data lake for both raw and processed data.
* **boto3:** Python SDK for AWS, used to interact with S3 from the transformation script.
* **Data Transformation:** Hands-on experience with cleaning, filling missing data, and type casting using **pandas**.
* **ETL Concepts:** Practical application of the Ingest-Transform-Store pipeline.

---
**Connect with me:**

https://www.linkedin.com/feed/

Updated README to reflect cloud architecture using AWS S3.
