# sentiment.py
from transformers import pipeline

# Load sentiment model
sentiment_pipeline = pipeline('sentiment-analysis')

# Analyze sentiment
def analyze_sentiment(review_text):
    result = sentiment_pipeline(review_text)
    return result[0]['label']
