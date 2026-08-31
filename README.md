# du-university-chapters-pipeline
This project is a simple data pipeline that pulls university chapter information from the Ducks Unlimited API, cleans and checks the data, and saves it into Google BigQuery.



du-chapters-etl/
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # Optional CI/CD pipeline
├── src/
│   ├── __init__.py
│   ├── extract.py             # Extraction logic from API / files
│   ├── transform.py           # Data cleansing and transformation
│   ├── load.py                # BigQuery loading logic
│   └── pipeline.py            # Main orchestration script
├── tests/
│   ├── __init__.py
│   ├── test_transform.py      # Unit tests for transformation & validation
│   └── test_pipeline.py       # Integration tests
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Containerization for reproducibility
├── README.md                  # Comprehensive documentation
└── .env.example               # Template for environment variables
