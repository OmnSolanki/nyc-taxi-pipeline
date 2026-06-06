import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://localhost/nyc_taxi")

print("Loading raw data from PostgreSQL...")
df = pd.read_sql("SELECT * FROM raw_trips", engine)
print(f"Raw rows: {len(df)}")

# Drop nulls
df = df.dropna()

# Remove invalid trips
df = df[df['trip_distance'] > 0]
df = df[df['fare_amount'] > 0]
df = df[df['passenger_count'] > 0]
df = df[df['total_amount'] > 0]

# Remove outliers
df = df[df['trip_distance'] < 100]
df = df[df['fare_amount'] < 500]

# Add derived columns
df['trip_duration_min'] = (
    pd.to_datetime(df['tpep_dropoff_datetime']) - 
    pd.to_datetime(df['tpep_pickup_datetime'])
).dt.total_seconds() / 60

df['pickup_hour'] = pd.to_datetime(df['tpep_pickup_datetime']).dt.hour
df['pickup_day'] = pd.to_datetime(df['tpep_pickup_datetime']).dt.day_name()

# Remove invalid durations
df = df[df['trip_duration_min'] > 0]
df = df[df['trip_duration_min'] < 180]

print(f"Clean rows: {len(df)}")

# Save to PostgreSQL
print("Saving cleaned data...")
df.to_sql("cleaned_trips", engine, if_exists="replace", index=False)
print("Done!")