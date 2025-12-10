import pandas as pd
import os

def download_data():
    os.makedirs("data", exist_ok=True)
    df = pd.DataFrame({
        "feature1": [1,2,3,4,5],
        "feature2": [5,4,3,2,1],
        "month": ["JAN","FEB","MAR","APR","MAY"]
    })
    df.to_csv("data/raw_dataset.csv", index=False)
    print("Dataset downloaded.")

def clean_data():
    df = pd.read_csv("data/raw_dataset.csv")
    df.dropna(inplace=True)
    df.to_csv("data/cleaned_dataset.csv", index=False)
    print("Dataset cleaned.")
