import os
from dotenv import load_dotenv

load_dotenv()

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DATA_PATH = os.path.join(BASE_DIR, 'data/raw/sample_app_usage.csv')
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, 'data/processed/processed_app_usage.csv')

# Database config (we'll use later)
DB_CONFIG = {
    'dbname': os.getenv('DB_NAME', 'app_usage_db'),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', 'password'),
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', '5432')
}