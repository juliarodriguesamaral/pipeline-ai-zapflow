import random
import logging
from faker import Faker
import database

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SalesDataGenerator:
    def __init__(self, db_connection, batch_size=100):
        self.conn, self.cursor = db_connection
        self.batch_size = batch_size
        self.fake = Faker()
        self.products = [
            "Zapflow with Gemini", 
            "Zapflow with chatGPT", 
            "Zapflow with Llama 3.0"
        ]

    def generate_sales_data(self, total_records):
        for i in range(total_records):
            record = self._generate_record()
            self._insert_record(record)
            
            if (i + 1) % self.batch_size == 0:
                self._commit_batch(i + 1)

        self.conn.commit()
        logging.info("Todos os registros foram inseridos com sucesso.")

    def _generate_record(self):
        email = self.fake.email()
        date = self.fake.date_between(start_date="-1y", end_date="today")
        price = round(random.uniform(10.0, 1000.0), 2)
        quantity = random.randint(1, 20)
        product = random.choice(self.products)
        return (email, date, price, quantity, product)

    def _insert_record(self, record):
        self.cursor.execute(
            """
            INSERT INTO sales (email, date, price, quantity, product)
            VALUES (%s, %s, %s, %s, %s)
            """,
            record
        )

    def _commit_batch(self, record_count):
        self.conn.commit()
        logging.info(f"{record_count} registros inseridos com sucesso.")

    def close_connection(self):
        self.cursor.close()
        self.conn.close()


def main():
    db_connection = database.connect_in_database()
    generator = SalesDataGenerator(db_connection, batch_size=100)

    try:
        generator.generate_sales_data(10000)

    finally:
        generator.close_connection()


if __name__ == "__main__":
    main()
