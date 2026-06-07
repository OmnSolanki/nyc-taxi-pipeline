with trips as (
    select * from {{ ref('stg_trips') }}
),

summary as (
    select
        pickup_hour,
        pickup_day,
        payment_type,
        count(*)                    as total_trips,
        round(avg(trip_distance)::numeric, 2)   as avg_distance,
        round(avg(fare_amount)::numeric, 2)     as avg_fare,
        round(avg(tip_amount)::numeric, 2)      as avg_tip,
        round(sum(total_amount)::numeric, 2)    as total_revenue,
        round(avg(trip_duration_min)::numeric, 2) as avg_duration_min
    from trips
    group by pickup_hour, pickup_day, payment_type
)

select * from summary