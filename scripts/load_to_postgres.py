import pandas as pd
from sqlalchemy import create_engine

# Load raw parquet file
print("Loading data...")
df = pd.read_parquet("data/raw/yellow_tripdata_2024-01.parquet")

print(f"Rows: {len(df)}")
print(f"Columns: {list(df.columns)}")
print(df.head())

# Connect to PostgreSQL
engine = create_engine("postgresql://localhost/nyc_taxi")

# Load into PostgreSQL
print("Loading into PostgreSQL...")
df.to_sql("raw_trips", engine, if_exists="replace", index=False)
print("Done!")