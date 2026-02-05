import pandas as pd

def load_movies(path="../data/movies.csv"):
    return pd.read_csv(path)

def load_ratings(path="../data/ratings.csv"):
    return pd.read_csv(path)
