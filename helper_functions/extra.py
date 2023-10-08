import pandas as pd

def load_file(path):
    with open(path) as file:
        df = pd.read_csv(file, parse_dates=True)
        return df