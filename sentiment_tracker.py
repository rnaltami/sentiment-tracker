import nltk
import os
import sys  # <-- Add this back

# Explicitly set the NLTK data path
nltk.data.path.append(os.path.expanduser("~/nltk_data"))

from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Function to analyze sentiment
def analyze_sentiment(text):
    sentiment_score = sia.polarity_scores(text)
    if sentiment_score['compound'] >= 0.05:
        return "Positive 😊"
    elif sentiment_score['compound'] <= -0.05:
        return "Negative 😡"
    else:
        return "Neutral 😐"

# Get user input or command-line input
if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_input = " ".join(sys.argv[1:])
    else:
        user_input = input("Enter a sentence to analyze sentiment: ")

    result = analyze_sentiment(user_input)
    print(f"Sentiment: {result}")
