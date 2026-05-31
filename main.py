from extract import extract_app_usage
from transform import transform_app_usage
from load import load_to_postgres
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/etl.log", encoding='utf-8'),
        logging.StreamHandler()
    ]
)

if __name__ == "__main__":
    print("=" * 70)
    print("     APPLICATION USAGE ANALYTICS PIPELINE")
    print("=" * 70)
    
    try:
        print("\n🚀 Starting Full ETL Pipeline...\n")
        
        # Extract
        df_raw = extract_app_usage()
        
        # Transform
        df_clean = transform_app_usage(df_raw)
        
        # Load
        load_to_postgres(df_clean)
        
        print("\n" + "=" * 70)
        print("🎉 FULL PIPELINE COMPLETED SUCCESSFULLY!")
        print("=" * 70)
        
    except Exception as e:
        print(f"\n❌ Pipeline failed: {e}")