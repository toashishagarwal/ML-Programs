# data_generator.py

import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

def generate_customer_data(n=1000):
    data = []
    for i in range(n):
        customer_id = f"C{i:06d}"
        gender = random.choice(['Male', 'Female'])
        age = random.randint(18, 75)
        location = fake.city()
        tenure_months = random.randint(1, 72)
        contract_type = random.choices(['Month-to-Month', 'One year', 'Two year'], weights=[0.6, 0.25, 0.15])[0]
        payment_method = random.choice(['Credit Card', 'Debit Card', 'Auto-pay', 'Bank Transfer'])
        monthly_charge = round(random.uniform(20, 120), 2)
        total_charge = round(monthly_charge * tenure_months + random.uniform(-20, 20), 2)
        churned = random.choices([1, 0], weights=[0.3, 0.7])[0]
        data.append([customer_id, gender, age, location, tenure_months, contract_type, payment_method,
                     monthly_charge, total_charge, churned])
    return pd.DataFrame(data, columns=[
        'customer_id', 'gender', 'age', 'location',
        'tenure_months', 'contract_type', 'payment_method',
        'monthly_charge', 'total_charge', 'churned'
    ])

def generate_usage_data(customers_df):
    usage_data = []
    for cid in customers_df['customer_id']:
        call_minutes = max(0, round(np.random.normal(350, 50), 2))
        data_usage_gb = max(0, round(np.random.normal(7, 2), 2))
        sms_usage = random.randint(50, 800)
        num_complaints = np.random.poisson(0.4)
        usage_data.append([cid, call_minutes, data_usage_gb, sms_usage, num_complaints])
        
    return pd.DataFrame(usage_data, columns=['customer_id', 'call_minutes', 'data_usage_gb',
                                             'sms_usage', 'num_complaints'])

def generate_full_dataset(n=1000):
    customers = generate_customer_data(n)
    usage = generate_usage_data(customers)
    full_df = pd.merge(customers, usage, on='customer_id')
    return full_df

if __name__ == "__main__":
    df = generate_full_dataset(1000)
    df.to_csv("churn_dataset.csv", index=False)
    print("Synthetic data saved to churn_dataset.csv")
