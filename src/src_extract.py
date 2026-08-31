import os
import pandas as pd
import requests

def extract_from_csv(file_path: str) -> list:
    """Extracts raw chapter data from a local CSV file (kept for fallback/local testing)."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Source file not found at: {file_path}")
    
    df = pd.read_csv(file_path)
    return df.to_dict(orient="records")

def extract_from_api(api_url: str) -> list:
    """Extracts raw chapter data from the external ArcGIS REST API endpoint."""
    params = {
        "where": "1=1",
        "outFields": "*",
        "outSR": "4326",
        "f": "json"
    }
    
    response = requests.get(api_url, params=params, timeout=30)
    response.raise_for_status()
    
    data = response.json()
    return data if isinstance(data, list) else data.get("features", [])