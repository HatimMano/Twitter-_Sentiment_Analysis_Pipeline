import time
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from kafka import KafkaConsumer
import json

def fetch_latest_sentiment_data():
    # Connect to Kafka and consume sentiment data
    consumer = KafkaConsumer('sentiment_topic', bootstrap_servers=['localhost:9092'])
    sentiment_data = []

    # Fetch the latest sentiment data
    for message in consumer:
        sentiment_data.append(json.loads(message.value.decode('utf-8')))
        if len(sentiment_data) >= 100:  # Limit to 100 records
            break

    return sentiment_data


def create_dashboard(sentiment_data):
    # Extract sentiment scores and timestamps from the data
    sentiment_scores = [record['sentiment_score'] for record in sentiment_data]
    timestamps = [record['timestamp'] for record in sentiment_data]

    # Create a Plotly figure with two subplots (one for sentiment scores and one for tweet count)
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Sentiment Analysis", "Tweet Count"))

    # Add trace for sentiment scores over time
    fig.add_trace(go.Scatter(x=timestamps, y=sentiment_scores, mode='lines', name='Sentiment Score'), row=1, col=1)

    # Update layout
    fig.update_layout(title='Real-time Twitter Sentiment Analysis Dashboard',
                      xaxis=dict(title='Timestamp'),
                      yaxis=dict(title='Sentiment Score'),
                      template='plotly_dark')

    # Show the dashboard
    fig.show()


def fetch_latest_tweet_data():
    # Connect to Kafka and consume tweet data
    consumer = KafkaConsumer('tweet_topic', bootstrap_servers=['localhost:9092'])
    tweet_data = []

    # Fetch the latest tweet data
    for message in consumer:
        tweet_data.append(json.loads(message.value.decode('utf-8')))
        if len(tweet_data) >= 100:  # Limit to 100 records
            break

    return tweet_data

def generate_reports(tweet_data):
    # Placeholder function to generate reports
    # Convert tweet data to DataFrame for easier manipulation
    df = pd.DataFrame(tweet_data)

    # Calculate aggregate statistics (e.g., average sentiment score, tweet count) over different time intervals
    average_sentiment_by_hour = df.groupby(df['timestamp'].dt.hour)['sentiment_score'].mean()
    tweet_count_by_day = df.groupby(df['timestamp'].dt.date).size()

    # Generate summary reports or analytics based on the aggregate statistics
    average_sentiment_report = f"Average Sentiment by Hour:\n{average_sentiment_by_hour}\n"
    tweet_count_report = f"Tweet Count by Day:\n{tweet_count_by_day}\n"

    # Write reports to files or send them via email, etc.
    with open('average_sentiment_report.txt', 'w') as f:
        f.write(average_sentiment_report)
    
    with open('tweet_count_report.txt', 'w') as f:
        f.write(tweet_count_report)

# Main loop for periodic execution
while True:
    # Update the dashboard periodically
    sentiment_data = fetch_latest_sentiment_data()
    create_dashboard(sentiment_data)

    # Generate reports periodically
    tweet_data = fetch_latest_tweet_data()
    generate_reports(tweet_data)

    # Wait for a certain interval before updating the dashboard and generating reports again
    time.sleep(300)  # Wait for 5 minutes before updating the dashboard and generating reports again
