"""
Configuration File

This file contains various configurations used in the data processing pipeline.

Attributes:
    text_column_to_use (str): The name of the column in the dataset containing text data.
    vectorized_text_column (str): The name of the column to store vectorized text data.
    spacy_model (str): The name of the spaCy language model used for text processing.
    custom_stop_words (set): A set of custom stop words to be excluded during text processing.


    MORE ATTRIBUTES TO COME :)
"""

text_column_to_use = 'summary'

vectorized_text_column = text_column_to_use + '_vectorized'

spacy_model = 'en_core_web_lg'

custom_stop_words = {'a', 'about', 'above', 'against', 'am', 'an', 'and', 'any', 'are', 'as',
                     'at',
                     'been', 'below', 'between', 'both', 'by', 'could', 'd', 'does',
                     'doing', 'each', 'for', 'from', 'further', 'he', 'her',
                     'here', 'hers', 'herself', 'him', 'himself', 'his', 'i', 'into', 'it', "it's", 'its',
                     'itself',
                     'just', 'll', 'm', 'me', 'my', 'myself', 'nor', 'now', 'o', 'of', 'off', 'once',
                     'or', 'other', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 're', 's', 'same', 'she',
                     "she's", 'should',
                     'so', 'some', 'such', 't', 'than', 'that', "that'll", 'the', 'their', 'theirs', 'them',
                     'themselves', 'then', 'there',
                     'these', 'they', 'this', 'those', 'through', 'too', 'under', 'until', 'up', 've', 'we',
                     'were', 'to'
                     'what',
                     'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'would', 'y',
                     'you',
                     "you'd", "you'll",
                     "you're", "you've", 'your', 'yours', 'yourself', 'yourselves'
                     "gt", "lt"  # These two could be used to produce a new abstraction since they are > and < respectively
                     }
