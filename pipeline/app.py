import streamlit as st
from datetime import datetime
from pipeline.data_contract import Sales
from pydantic import ValidationError
from pipeline.database import save_sales_data

def main ():
    st.title("ZapFlow CRM and Sales System")
    email = st.text_input("Salesperson email")
    date = st.date_input("Date of sale")
    time = st.time_input("Time of sale")
    product = st.selectbox("Product", ["Zapflow with Gemini", "Zapflow with chatGPT", "Zapflow with Llama 3.0"])
    price = st.number_input("Product price", min_value=0.0, format="%.2f")
    quantity = st.number_input("Product quantity", min_value=0)

    if st.button("Salvar"):
        date_time= datetime.combine(date, time)
        create_and_validate_sale(email, date_time, product, price, quantity)

def create_and_validate_sale(email, date_time, product, price, quantity):
    try:
        sale = Sales(
            email = email,
            date = date_time,
            product = product,
            price = price,
            quantity = quantity
        )
        save_sales_data(sale)
        
    except ValidationError as e:
        st.error(f"Try again. Error {e}")
        

if __name__=="__main__":
    main()