# Retail Customer Segmentation

A Python project to segment retail customers using RFM (Recency, Frequency, Monetary) features and clustering techniques.
The program uses K-means clustering to segment the customers and stores the model file in models/kmeans_model.pkl file

## Features
- Synthetic data generation (customers, products, transactions)
- RFM feature engineering
- K-Means Clustering
- SQLite-based storage

## Setup Instructions ##
1. python -m venv cluster-env
2. source cluster-env/bin/activate
3. pip install -r requirements.txt

## Run Instruction s##
1. python3.9 main.py
