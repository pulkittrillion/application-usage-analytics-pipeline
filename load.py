import pandas as pd
import psycopg2
from psycopg2.extras import execute_values
import logging
from dotenv import load_dotenv
import os
from transform import transform_app_usage

load_dotenv()

# Database Configuration
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "database": os.getenv("DB_NAME", "app_usage_db"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD"),
    "port": os.getenv("DB_PORT", "5432")
}

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/etl.log", encoding='utf-8'),
        logging.StreamHandler()
    ]
)

def load_to_postgres(df=None):
    """Load transformed application usage data into PostgreSQL"""
    if df is None:
        df = transform_app_usage()
    
    logging.info("Starting load to PostgreSQL...")
    
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        # Create table if not exists
        create_table_query = """
        CREATE TABLE IF NOT EXISTS app_usage (
            id SERIAL PRIMARY KEY,
            date DATE,
            employee_id VARCHAR(20),
            branch VARCHAR(50),
            department VARCHAR(50),
            total_tasks INTEGER,
            app_tasks INTEGER,
            manual_tasks INTEGER,
            app_name VARCHAR(100),
            adoption_rate NUMERIC(5,2),
            manual_rate NUMERIC(5,2),
            efficiency_score NUMERIC(5,2),
            adoption_category VARCHAR(20),
            loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        cur.execute(create_table_query)

        # Prepare data
        df_load = df.copy()
        df_load['date'] = pd.to_datetime(df_load['date']).dt.date

        # Convert to tuples
        tuples = [tuple(x) for x in df_load[[
            'date', 'employee_id', 'branch', 'department', 'total_tasks',
            'app_tasks', 'manual_tasks', 'app_name', 'adoption_rate',
            'manual_rate', 'efficiency_score', 'adoption_category'
        ]].values]

        # Insert query
        insert_query = """
        INSERT INTO app_usage (
            date, employee_id, branch, department, total_tasks, app_tasks,
            manual_tasks, app_name, adoption_rate, manual_rate,
            efficiency_score, adoption_category
        ) VALUES %s
        """
        
        execute_values(cur, insert_query, tuples)
        conn.commit()

        logging.info(f"✅ Successfully loaded {len(df_load)} records into 'app_usage' table")
        print(f"✅ Successfully loaded {len(df_load)} records into PostgreSQL!")

        cur.close()
        conn.close()

    except Exception as e:
        logging.error(f"❌ Load failed: {str(e)}")
        print(f"❌ Error: {str(e)}")
        raise

# For testing
if __name__ == "__main__":
    load_to_postgres()