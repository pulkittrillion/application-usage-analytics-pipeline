import pandas as pd
import os
from config import RAW_DATA_PATH

def extract_app_usage():
    """
    Extract raw application usage data from CSV file.
    Returns:
        pandas.DataFrame: Raw application usage data
    """
    try:
        if not os.path.exists(RAW_DATA_PATH):
            raise FileNotFoundError(f"Raw data file not found at: {RAW_DATA_PATH}")
        
        df = pd.read_csv(RAW_DATA_PATH)
        
        # Basic validation
        required_columns = ['date', 'employee_id', 'branch', 'department', 
                          'total_tasks', 'app_tasks', 'manual_tasks', 'app_name']
        
        missing_cols = [col for col in required_columns if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")
        
        print(f"✅ Successfully extracted {len(df)} records from {RAW_DATA_PATH}")
        return df
        
    except Exception as e:
        print(f"❌ Error extracting data: {str(e)}")
        raise


# For testing
if __name__ == "__main__":
    df = extract_app_usage()
    print("\nFirst 5 rows:")
    print(df.head())
    print("\nData Info:")
    print(df.info())