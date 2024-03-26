# Real-time Twitter Sentiment Analysis Pipeline

## Overview

This project aims to build a real-time data pipeline to perform sentiment analysis on live tweets streamed from Twitter. The pipeline extracts tweets using the Twitter API, preprocesses them, performs sentiment analysis, and stores the results in a database for further analysis and visualization.

## Components

### 1. Data Extraction (Guided)

- **File**: `data_extraction/twitter_api.py`
- **Description**: Connects to the Twitter API and streams live tweets containing specific keywords or hashtags.

### 2. Data Processing

- **File**: `data_processing/preprocess_tweets.py`
- **Description**: Preprocesses raw tweet data by removing special characters, URLs, and non-alphanumeric characters.

- **File**: `data_processing/sentiment_analysis.py`
- **Description**: Performs sentiment analysis on the preprocessed tweet text to determine the sentiment (positive, negative, or neutral).

### 3. Real-time Processing

- **File**: `real_time_processing/kafka_ingestion.py`
- **Description**: Ingests data from the Twitter API into Kafka topics for real-time processing.

- **File**: `real_time_processing/stream_processing.py`
- **Description**: Processes data streams in real-time using Apache Kafka, performs sentiment analysis, and sends the processed data to a database.

### 4. Visualization and Reporting

- **File**: `visualization_reporting/dashboard_visualization.py`
- **Description**: Creates interactive dashboards for visualizing real-time sentiment analysis results.

- **File**: `visualization_reporting/periodic_reports.py`
- **Description**: Generates periodic reports or analytics based on stored tweet data.

## Usage

1. **Clone the Repository**:

2. **Set Up Twitter API Credentials**:
- Obtain Twitter API credentials from the Twitter Developer Dashboard.
- Replace the placeholders in `data_extraction/twitter_api.py` with your credentials.

3. **Install Dependencies**:
- Navigate to each component directory and install the required dependencies using the provided `requirements.txt` files.

4. **Run the Pipeline**:
- Execute each component of the pipeline sequentially to extract, process, store, and visualize real-time sentiment analysis results.

