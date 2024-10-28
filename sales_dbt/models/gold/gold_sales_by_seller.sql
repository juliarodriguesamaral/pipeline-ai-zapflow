{{ config(materialized='view') }}

WITH sales_by_seller AS (
    SELECT 
        email AS seller, 
        DATE(date) AS date, 
        SUM(price) AS total_sales_value, 
        SUM(quantity) AS total_quantity_sold, 
        COUNT(*) AS total_sales_count
    FROM 
        {{ ref('silver_sales') }}
    WHERE 
        date >= CURRENT_DATE - INTERVAL '30 days'
    GROUP BY 
        email, DATE(date)
)

SELECT 
    seller, 
    date, 
    total_sales_value, 
    total_quantity_sold, 
    total_sales_count
FROM 
    sales_by_seller
ORDER BY 
    date ASC, seller ASC