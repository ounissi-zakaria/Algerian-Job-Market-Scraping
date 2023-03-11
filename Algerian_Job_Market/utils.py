import pandas as pd


def load_jobs(load_from: str):
    for idx, row in pd.read_csv(load_from).iterrows():
        yield row
