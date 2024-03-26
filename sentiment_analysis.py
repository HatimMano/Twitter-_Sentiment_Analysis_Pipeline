from textblob import TextBlob

def analyze_sentiment(tweet_text):
    # Perform sentiment analysis using TextBlob
    blob = TextBlob(tweet_text)
    sentiment_score = blob.sentiment.polarity
    return sentiment_score
