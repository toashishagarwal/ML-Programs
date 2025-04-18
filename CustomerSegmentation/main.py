# main.py
from src import database, generate_data, feature_engineering, clustering
import pandas as pd

def main():
    print("Setting up database...")
    database.create_schema()

    print("Generating synthetic data...")
    generate_data.generate_customers()
    generate_data.generate_products()
    generate_data.generate_transactions()

    print("Extracting features...")
    df = feature_engineering.build_features()

    print("Running clustering...")
    df_segmented = clustering.train_kmeans(df, k=4)

    print("Top 5 segmented customers:")
    print(df_segmented[['customer_id', 'segment']].head())

    # Optional: Save segments
    conn = database.get_connection()
    df_segmented[['customer_id', 'segment']].to_sql('customer_segments', conn, if_exists='replace', index=False)
    conn.close()

if __name__ == '__main__':
    main()
