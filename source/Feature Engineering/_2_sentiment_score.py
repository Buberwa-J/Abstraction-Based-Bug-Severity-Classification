from textblob import TextBlob
import pandas as pd
from source.configurations import text_column_to_use

merged_df = pd.read_csv(r'../../datasets/cleaned datasets/merged_cleaned.csv')


def get_sentiment_score(text):
    blob = TextBlob(text)
    # Calculate sentiment score using TextBlob's polarity attribute
    sentiment_score = blob.sentiment.polarity
    return sentiment_score


new_df = pd.DataFrame()
new_df['sentiment_score'] = merged_df[text_column_to_use].apply(get_sentiment_score)

# Normalize sentiment scores to the range [-1, 1] for the dataset
max_sentiment_score = new_df['sentiment_score'].max()
min_sentiment_score = new_df['sentiment_score'].min()
new_df['normalized_sentiment'] = (new_df['sentiment_score'] - min_sentiment_score) / (max_sentiment_score - min_sentiment_score) * 2 - 1
new_df.drop(columns=['sentiment_score'], inplace=True)

new_df.to_csv(r'../../datasets/feature engineered datasets/sentiment_scores.csv', index=False)
