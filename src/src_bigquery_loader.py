import os
from google.cloud import bigquery
from google.cloud.exceptions import GoogleCloudError
import pandas as pd

def load_to_bigquery(df: pd.DataFrame, dataset_id: str, table_id: str = "university_chapters") -> None:
    """
    Loads the transformed pandas DataFrame into Google BigQuery.
    """
    client = bigquery.Client()
    full_table_id = f"{client.project}.{dataset_id}.{table_id}"

    # Define explicit schema to ensure data integrity
    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        schema=[
            bigquery.SchemaField("chapter_id", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("chapter_name", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("city", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("state", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("longitude", "FLOAT", mode="REQUIRED"),
            bigquery.SchemaField("latitude", "FLOAT", mode="REQUIRED"),
        ],
    )

    try:
        load_job = client.load_table_from_dataframe(df, full_table_id, job_config=job_config)
        load_job.result()  # Wait for the job to complete
        print(f"[SUCCESS] Loaded {load_job.output_rows} rows into BigQuery table {full_table_id}.")
    except GoogleCloudError as e:
        print(f"[ERROR] Failed to load data into BigQuery: {e}")
        raise
