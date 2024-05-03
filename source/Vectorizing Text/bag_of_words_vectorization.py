import pandas as pd
from source.configurations import text_column_to_use
from source.Classes.TFIDFVectorizer import TFIDFVectorizer

# Load the dataset
merged_df = pd.read_csv('../../datasets/cleaned datasets/merged_cleaned.csv')

# Initialize TFIDFVectorizer with the text column name
tfidf_vectorizer = TFIDFVectorizer()

# Vectorize the text data
vectorized_df = tfidf_vectorizer.vectorize_text(merged_df, text_column_to_use)

# Save the vectorized dataset to a new CSV file
TFIDFVectorizer.save_vectorized_data(vectorized_df, '../../datasets/vectorized datasets/tfidf_vectorized.csv')
