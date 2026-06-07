with source as (
    select * from {{ source('public', 'cleaned_trips') }}
),

staged as (
    select
        "VendorID"          as vendor_id,
        "tpep_pickup_datetime"  as pickup_datetime,
        "tpep_dropoff_datetime" as dropoff_datetime,
        "passenger_count"   as passenger_count,
        "trip_distance"     as trip_distance,
        "PULocationID"      as pickup_location_id,
        "DOLocationID"      as dropoff_location_id,
        "payment_type"      as payment_type,
        "fare_amount"       as fare_amount,
        "tip_amount"        as tip_amount,
        "total_amount"      as total_amount,
        "trip_duration_min" as trip_duration_min,
        "pickup_hour"       as pickup_hour,
        "pickup_day"        as pickup_day
    from source
)

select * from staged