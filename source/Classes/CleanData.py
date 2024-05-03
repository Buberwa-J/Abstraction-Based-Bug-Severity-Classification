import spacy
from source.configurations import spacy_model, custom_stop_words


class CleanData:
    """
    A class to clean text data using spaCy.

    Attributes:
        nlp_model (spacy.lang): The spaCy language model.
        stop_words (list): List of custom stop words. I have defined it in the configurations.py
    """
    def __init__(self):
        self.nlp_model = spacy.load(spacy_model)
        self.stop_words = custom_stop_words

    def clean_text(self, df, column_to_clean):
        """
        Clean the text in the specified column of the dataframe.

        Args:
            df (DataFrame): The dataframe containing text data.
            column_to_clean (str): The name of the column to clean.
        """
        # Drop rows with missing values
        df.dropna(axis=0, how='any', inplace=True)

        # Convert text to lowercase
        df[column_to_clean] = df[column_to_clean].str.lower()

        # Apply text cleaning function
        df[column_to_clean] = df[column_to_clean].apply(self.apply_clean_text)

    def apply_clean_text(self, text):
        """
        Apply text cleaning operations using spaCy.

        Args:
            text (str): The input text to clean.

        Returns:
            str: The cleaned text.
        """
        doc = self.nlp_model(text)

        # Extract lemmatized tokens
        lemmatized_tokens = [token.lemma_ for token in doc]

        # Remove stop words
        cleaned_text = [word for word in lemmatized_tokens if word not in self.stop_words]

        # Join cleaned tokens into a single string
        cleaned_text = ' '.join(cleaned_text)
        return cleaned_text
