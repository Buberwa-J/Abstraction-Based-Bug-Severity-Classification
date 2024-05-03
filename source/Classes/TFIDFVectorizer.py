from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd


class TFIDFVectorizer:
    def __init__(self):
        self.tfidf_vectorizer = TfidfVectorizer(
            stop_words='english',
            min_df=0.01,  # Ignore terms that appear in less than 0.1% of the document
            max_features=500  # Limit the number of features to the top 500 most frequent terms
        )

    def vectorize_text(self, df, column_to_vectorize):
        """
        Vectorizes the text data in the DataFrame using TF-IDF vectorization.

        Args:
            df (pd.DataFrame): DataFrame containing the text data.
            column_to_vectorize (str): The name of the column to vectorize

        Returns:
            pd.DataFrame: DataFrame with TF-IDF vectorized text data.
        """
        # Apply TF-IDF vectorization to the text column
        X_tfidf = self.tfidf_vectorizer.fit_transform(df[column_to_vectorize])

        # Convert the sparse matrix to a DataFrame
        tfidf_df = pd.DataFrame(X_tfidf.toarray(), columns=self.tfidf_vectorizer.get_feature_names_out())

        return tfidf_df

    @staticmethod
    def save_vectorized_data(df, filename):
        """
        Saves the vectorized DataFrame to a CSV file.

        Args:
            df (pd.DataFrame): DataFrame containing the vectorized data.
            filename (str): Name of the CSV file to save.
        """
        df.to_csv(filename, index=False)

