# src/feature_engineering.py
import pandas as pd
from src.database import get_connection

def build_features():
    conn = get_connection()
    
    query = """
    WITH txn_summary AS (
        SELECT
            c.customer_id,
            MAX(t.transaction_date) as last_date,
            COUNT(t.transaction_id) as frequency,
            SUM(t.amount) as monetary
        FROM customers c
        LEFT JOIN transactions t ON c.customer_id = t.customer_id
        GROUP BY c.customer_id
    )
    SELECT 
        c.customer_id,
        JULIANDAY('now') - JULIANDAY(ts.last_date) AS recency,
        ts.frequency,
        ts.monetary,
        c.age,
        c.income
    FROM customers c
    JOIN txn_summary ts ON c.customer_id = ts.customer_id
    """
    
    df = pd.read_sql(query, conn)
    df.fillna({'recency': 999, 'frequency': 0, 'monetary': 0}, inplace=True)
    conn.close()
    return df
