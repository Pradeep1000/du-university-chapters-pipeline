# Ducks Unlimited University Chapters ETL Pipeline

## Project Overview
This project is a simple, modular data pipeline that pulls university chapter information from the Ducks Unlimited API, cleans and validates the attributes, and loads them downstream into Google BigQuery.

## Repository Structure

```text
du-chapters-etl/
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # Optional CI/CD pipeline
├── src/
│   ├── __init__.py
│   ├── extract.py             # Extraction logic from API
│   ├── transform.py           # Data cleansing and validation
│   ├── load.py                # BigQuery loading logic
│   └── pipeline.py            # Main orchestration script
├── tests/
│   ├── __init__.py
│   ├── test_transform.py      # Unit tests for transformation
│   └── test_pipeline.py       # Integration tests
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Containerization for reproducibility
├── README.md                  # Comprehensive documentation
└── .env.example               # Template for environment variables


## Architecture / Flow

1. **Extract (`extract.py`)**: Fetches raw JSON payload from the Ducks Unlimited public ArcGIS API endpoint.


2. **Transform (`transform.py`)**: Parses fields, cleans attribute mappings, validates data types, and extracts geographical coordinates (longitude and latitude).


3. **Load (`load.py`)**: Connects to Google Cloud and securely loads the clean records into BigQuery.


## Implementation Details & Workflow

The pipeline is structured modularly to ensure clean separation of concerns, robust error handling, and ease of testing:

* **Extraction (`extract.py`)**: Connects to the public Ducks Unlimited ArcGIS API endpoint to pull raw university chapter data.
* **Transformation (`transform.py`)**: Cleans, parses, and validates attributes (such as chapter IDs, names, cities, states, and coordinates) to enforce data quality before loading.
* **Loading (`load.py`)**: Establishes a secure connection to Google Cloud and writes the validated records downstream into Google BigQuery.
* **Orchestration (`pipeline.py`)**: Acts as the main entry point, tying extraction, transformation, and loading into a single automated end-to-end execution flow.
* **Testing (`tests/`)**: Implements unit and integration tests using `pytest` to verify transformation rules and validate pipeline behavior locally.
* **CI/CD Pipeline (`ci-cd.yml`)**: Automates testing and code quality checks using GitHub Actions upon pushing changes to the repository.

