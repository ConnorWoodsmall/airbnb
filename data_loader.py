import pandas as pd
import gzip
from io import BytesIO
import requests

def load_airbnb_data():
    url = 'https://data.insideairbnb.com/united-states/tx/dallas/2025-04-16/data/listings.csv.gz'
    response = requests.get(url)
    compressed_file = BytesIO(response.content)
    decompressed_file = gzip.GzipFile(fileobj = compressed_file)
    df = pd.read_csv(decompressed_file)
    return df

