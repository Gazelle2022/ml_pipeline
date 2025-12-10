import pandas as pd
import requests
import os

DATA_URL = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
DATA_PATH = "data/dataset.csv"

def download_data():
    response = requests.get(DATA_URL)
    os.makedirs("data", exist_ok=True)
    with open(DATA_PATH, "wb") as f:
        f.write(response.content)
    print("Dataset downloaded.")

def clean_data():
    df = pd.read_csv(DATA_PATH)
    df.dropna(axis=1, how='all', inplace=True)
    df.to_csv(DATA_PATH, index=False)
    print("Dataset cleaned.")

if __name__ == "__main__":
    download_data()
    clean_data()
