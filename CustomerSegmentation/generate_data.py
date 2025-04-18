# src/generate_data.py
import random
import numpy as np
from faker import Faker
from src.database import get_connection

fake = Faker()
random.seed(42)
np.random.seed(42)

def generate_customers(n=500):
    genders = ['Male', 'Female']
    locations = ['New York', 'Chicago', 'SF', 'Houston', 'Miami']

    conn = get_connection()
    cursor = conn.cursor()

    for _ in range(n):
        name = fake.name()
        gender = random.choice(genders)
        age = random.randint(18, 70)
        income = round(random.uniform(25000, 150000), 2)
        location = random.choice(locations)

        cursor.execute('''
            INSERT INTO customers (name, gender, age, income, location)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, gender, age, income, location))

    conn.commit()
    conn.close()

def generate_products(n=100):
    categories = ['Electronics', 'Clothing', 'Books', 'Furniture', 'Toys', 'Groceries']
    
    conn = get_connection()
    cursor = conn.cursor()

    for _ in range(n):
        category = random.choice(categories)
        price = round(random.uniform(5, 500), 2)
        cursor.execute('''
            INSERT INTO products (category, price)
            VALUES (?, ?)
        ''', (category, price))

    conn.commit()
    conn.close()

def generate_transactions(n=5000):
    conn = get_connection()
    cursor = conn.cursor()

    for _ in range(n):
        customer_id = random.randint(1, 500)
        product_id = random.randint(1, 100)
        cursor.execute('SELECT price FROM products WHERE product_id=?', (product_id,))
        price = cursor.fetchone()[0]
        quantity = random.randint(1, 5)
        amount = round(price * quantity, 2)
        date = fake.date_between(start_date='-1y', end_date='today')

        cursor.execute('''
            INSERT INTO transactions (customer_id, product_id, amount, quantity, transaction_date)
            VALUES (?, ?, ?, ?, ?)
        ''', (customer_id, product_id, amount, quantity, date))

    conn.commit()
    conn.close()
