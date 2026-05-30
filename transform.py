import pandas as pd
from extract import extract_app_usage

def transform_app_usage(df=None):
    """
    Transform raw application usage data and calculate key metrics.
    """
    if df is None:
        df = extract_app_usage()
    
    # Create a copy to avoid modifying original
    df_transformed = df.copy()
    
    # Convert date to datetime
    df_transformed['date'] = pd.to_datetime(df_transformed['date'])
    
    # Calculate key metrics
    df_transformed['adoption_rate'] = (df_transformed['app_tasks'] / df_transformed['total_tasks'] * 100).round(2)
    df_transformed['manual_rate'] = (df_transformed['manual_tasks'] / df_transformed['total_tasks'] * 100).round(2)
    
    # Efficiency Score (example: higher app usage = higher efficiency)
    df_transformed['efficiency_score'] = (df_transformed['adoption_rate'] * 0.7 + 
                                        (100 - df_transformed['manual_rate']) * 0.3).round(2)
    
    # Categorize adoption level
    def adoption_category(rate):
        if rate >= 90:
            return "Excellent"
        elif rate >= 70:
            return "Good"
        elif rate >= 50:
            return "Moderate"
        else:
            return "Low"
    
    df_transformed['adoption_category'] = df_transformed['adoption_rate'].apply(adoption_category)
    
    print(f"✅ Transformation completed. Processed {len(df_transformed)} records.")
    print("\nAdoption Rate Summary:")
    print(df_transformed['adoption_rate'].describe().round(2))
    
    return df_transformed


# For testing
if __name__ == "__main__":
    df_transformed = transform_app_usage()
    print("\nTransformed Data Sample:")
    print(df_transformed.head())
    print("\nColumns:", df_transformed.columns.tolist())