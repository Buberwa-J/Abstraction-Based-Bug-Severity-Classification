from source.Classes.SpacyVectorizer import SpacyVectorizer
import pandas as pd
from source.configurations import text_column_to_use as column_to_vectorize
from source.configurations import spacy_model as vectorizer_model

# Load the dataset
merged_df = pd.read_csv(r'../../datasets/cleaned datasets/merged_cleaned.csv')

vectorizer = SpacyVectorizer(model=vectorizer_model)

vectorized_df = vectorizer.vectorize_text(merged_df, column_to_vectorize)

# Save the vectorized dataset to a new CSV file
SpacyVectorizer.save_vectorized_data(vectorized_df, '../../datasets/vectorized datasets/spacy_vectorized.csv')
