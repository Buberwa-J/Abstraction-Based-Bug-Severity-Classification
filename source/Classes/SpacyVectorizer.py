import spacy
import pandas as pd
from source.configurations import vectorized_text_column


class SpacyVectorizer:
    def __init__(self, model):
        """
        Initialize the Vectorizer object.

        Args:
            model (str): The name of the spaCy model to use for vectorization.
        """
        self.nlp = spacy.load(model)

    def apply_vectorize_text(self, text):
        """
        Apply vectorization to a single text.

        Args:
            text (str): The text to vectorize.

        Returns:
            numpy.ndarray: The vector representation of the text.
        """
        return self.nlp(text).vector

    def vectorize_text(self, dataframe, column_to_vectorize):
        """
        Vectorize a column of text in a DataFrame and add the vectorized representation as a new column.

        Args:
            dataframe (pandas.DataFrame): The DataFrame containing the text data.
            column_to_vectorize (str): The name of the column to vectorize.
        Returns:
            pd.DataFrame: DataFrame with Spacy vectorized text data.
        """

        result_vectors = []
        for text in dataframe[column_to_vectorize]:
            result_vectors.append(self.apply_vectorize_text(text))
        vectorized_df = pd.DataFrame(result_vectors)
        return vectorized_df

    @staticmethod
    def save_vectorized_data(df, filename):
        """
        Saves the vectorized DataFrame to a CSV file.

        Args:
            df (pd.DataFrame): DataFrame containing the vectorized data.
            filename (str): Name of the CSV file to save.
        """
        df.to_csv(filename, index=False)
