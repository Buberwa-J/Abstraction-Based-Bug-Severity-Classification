import pandas as pd
from source.configurations import text_column_to_use

# Define the abstractions
abstractions = {
    'component': 'component',
    'exception': 'exception',
    'class': 'class',
    'method': 'method',
    'configuration file': 'configuration file',
    'source file': 'source file',
    'version number': 'version number',
    'variable': 'variable',
    'number': 'number',
    'error': 'error'
}

merged_df = pd.read_csv(f'../../datasets/cleaned datasets/merged_cleaned.csv')


def calculate_word_frequencies(summary):
    words = summary.lower().split()
    summary_length = len(words)
    frequencies = {}
    for key, value in abstractions.items():
        if ' ' in value:  # Check if multi-word abstraction
            value_parts = value.split()
            count = sum(1 for i in range(len(words) - len(value_parts) + 1) if words[i:i + len(value_parts)] == value_parts)
        else:
            count = words.count(value)
        frequencies[key + '_frequencies'] = count / summary_length  # Calculate frequency
    return frequencies


# Apply the function to each row in the DataFrame
new_df = pd.DataFrame()
new_df['word_frequencies'] = merged_df[text_column_to_use].apply(calculate_word_frequencies)

# Expand the dictionary into separate columns for training DataFrame
word_frequency_df = new_df['word_frequencies'].apply(pd.Series)

word_frequency_df.to_csv(r'../../datasets/feature engineered datasets/word_frequencies.csv', index=False)
