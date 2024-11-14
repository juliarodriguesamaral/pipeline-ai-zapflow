{{ config(materialized= 'view') }}

WITH cleaned_data AS (
    SELECT
        email,
        DATE(date) AS date,
        product,
        ROUND(CAST(price AS DECIMAL(10,2)) ,2) as price,
        quantity
    FROM
        {{ ref('bronze_sales') }}
    WHERE
        price > 0
        AND price < 8000
        AND date <= CURRENT_DATE


)

SELECT * FROM cleaned_data