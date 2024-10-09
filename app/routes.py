# routes.py
from flask import Flask, request, render_template
from app.recommender import load_data, train_recommender, recommend
from app.sentiment import analyze_sentiment

app = Flask(__name__)

# Load and train
movie_data = load_data('data/movies.csv')
model = train_recommender(movie_data)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend_movies():
    user_id = int(request.form['user_id'])
    top_movies = recommend(model, user_id, movie_data['movieId'].unique())
    return render_template('recommend.html', recommendations=top_movies)

@app.route('/sentiment', methods=['POST'])
def sentiment():
    review = request.form['review']
    sentiment_result = analyze_sentiment(review)
    return render_template('sentiment.html', sentiment=sentiment_result)
