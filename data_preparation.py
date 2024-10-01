# 1. data_preparation.py
import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    return df