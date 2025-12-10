from src.update_data import download_data, clean_data
from src.train_model import train_model

def test_pipeline():
    download_data()
    clean_data()
    train_model()
