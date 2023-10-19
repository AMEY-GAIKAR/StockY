import pandas as pd
from pathlib import Path

def load_file(path):
    with open(path) as file:
        df = pd.read_csv(file, parse_dates=True)
        return df

def create_file_list(dir):
    return list(Path(dir).glob('*'))

