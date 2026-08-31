import os
from dotenv import load_dotenv
from src.src_extract import extract_from_api, extract_from_csv
from src.src_transform import transform_chapters
from src.src_bigquery_loader import load_to_bigquery

# Load environment variables from a .env file if present
load_dotenv()

def run_pipeline():
    # Toggle between 'api' or 'csv' via environment variable (defaults to 'api' to meet requirements)
    SOURCE_TYPE = os.getenv("SOURCE_TYPE", "api").lower()
    
    BQ_DATASET_ID = os.getenv("BQ_DATASET_ID", "etl_pipeline")
    BQ_TABLE_ID = os.getenv("BQ_TABLE_ID", "university_chapters")

    print("[INFO] Step 1: Extracting data...")
    if SOURCE_TYPE == "csv":
        data_path = os.getenv("DATA_SOURCE_PATH", "data/DU_University_Chapters.csv")
        print(f"[INFO] Extracting from local CSV: {data_path}")
        raw_data = extract_from_csv(data_path)
    else:
        api_url = os.getenv(
            "DU_API_URL", 
            "https://services2.arcgis.com/5I7u4SJE1vUr79JC/arcgis/rest/services/UniversityChapters_Public/FeatureServer/0/query"
        )
        print(f"[INFO] Extracting from ArcGIS REST API")
        raw_data = extract_from_api(api_url)

    print("[INFO] Step 2: Transforming and validating data...")
    clean_df = transform_chapters(raw_data)

    print(f"[INFO] Step 3: Loading {len(clean_df)} records into BigQuery...")
    load_to_bigquery(clean_df, BQ_DATASET_ID, BQ_TABLE_ID)

    print("[INFO] ETL Pipeline executed successfully.")

if __name__ == "__main__":
    run_pipeline()