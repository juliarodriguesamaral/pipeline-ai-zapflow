{{ config(materialized='view') }}

WITH sales_last_7_days AS (
    SELECT
        date,
        product,
        SUM(price) AS total_sales_value,
        SUM(quantity) AS total_quantity_sold,
        COUNT(*) AS total_sales_count
    FROM
        {{ ref('silver_sales') }}
    WHERE
        date >= CURRENT_DATE - INTERVAL '30 days'
    GROUP BY
        date, product
)

SELECT
    date,
    product,
    total_sales_value,
    total_quantity_sold,
    total_sales_count
FROM 
    sales_last_7_days
ORDER BY date ASC
