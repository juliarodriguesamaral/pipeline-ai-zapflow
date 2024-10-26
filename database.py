import psycopg2
from psycopg2 import sql
from data_contract import Sales
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

def connect_in_database():
    conn = psycopg2.connect(
        host = DB_HOST,
        database = DB_NAME,
        user = DB_USER,
        password = DB_PASS,
        connect_timeout = 10 
    )
    cursor = conn.cursor()
    return conn, cursor

def save_sales_data(data: Sales):
    try:
        conn, cursor = connect_in_database()

        insert_query = sql.SQL(
        "INSERT INTO sales (email, date, product, price, quantity) VALUES(%s, %s, %s, %s, %s)"
        )
        cursor.execute(insert_query, (
            data.email,
            data.date,
            data.product.value,
            data.price,
            data.quantity
        ))
        conn.commit()
        cursor.close()
        conn.close()
        st.success("Data saved successfully!")
    except Exception as e:
        st.error(f"Error saving data: {e}")