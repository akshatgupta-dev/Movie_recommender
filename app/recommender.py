# recommender.py
import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split

# Load movie data
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Train the model
def train_recommender(data):
    reader = Reader(rating_scale=(1, 5))
    dataset = Dataset.load_from_df(data[['userId', 'movieId', 'rating']], reader)
    trainset, _ = train_test_split(dataset, test_size=0.2)
    model = SVD()
    model.fit(trainset)
    return model

# Recommend movies
def recommend(model, user_id, movie_ids, top_n=5):
    predictions = [(movie, model.predict(user_id, movie).est) for movie in movie_ids]
    predictions.sort(key=lambda x: x[1], reverse=True)
    return predictions[:top_n]
