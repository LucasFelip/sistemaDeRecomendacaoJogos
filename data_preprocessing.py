import pandas as pd

def preprocess_data(data):
    data['positive_ratings'] = pd.to_numeric(data['positive_ratings'], errors='coerce')
    data['negative_ratings'] = pd.to_numeric(data['negative_ratings'], errors='coerce')
    data.dropna(subset=['positive_ratings', 'negative_ratings'], inplace=True)
    return data