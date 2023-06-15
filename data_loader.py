import pandas as pd

def load_data():
    url = 'https://drive.google.com/uc?export=download&id=1SdCK7a5E9_vQKTEmMtEROrq-LBsKlTPE'
    data = pd.read_csv(url, dtype={'id': str}, low_memory=False)
    return data