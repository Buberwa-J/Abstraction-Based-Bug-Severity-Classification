"""
Dataset Encoding Script

This script reads datasets from CSV files, encodes type and priority columns and saves the encoded datasets.

Functions:
    encode_priority: Encodes the 'type' and 'priority' columns of a DataFrame into numerical values.
                      Saves the encoded DataFrame to a CSV file.

Attributes:
    ambari (DataFrame): DataFrame containing data from the Ambari dataset.
    camel (DataFrame): DataFrame containing data from the Camel dataset.
    derby (DataFrame): DataFrame containing data from the Derby dataset.
    wicket (DataFrame): DataFrame containing data from the Wicket dataset.
    datasets (list): A list of tuples containing dataset names and corresponding DataFrames.
"""
import pandas as pd
import os

ambari = pd.read_csv('../datasets/trimmed datasets/ambari.csv')
camel = pd.read_csv('../datasets/trimmed datasets/camel.csv')
derby = pd.read_csv('../datasets/trimmed datasets/derby.csv')
wicket = pd.read_csv('../datasets/trimmed datasets/wicket.csv')

datasets = [('ambari', ambari), ('camel', camel), ('derby', derby), ('wicket', wicket)]


def encode_priority(df, file_name):
    """
    Encode the 'type' and 'priority' columns of a DataFrame into numerical values.

    Args:
        df (DataFrame): The DataFrame to be encoded.
        file_name (str): The name of the file to save the encoded DataFrame.

    Returns:
        None
    """
    preliminary_encoded_datasets_dir = '../datasets/preliminary encoded datasets'

    df['type'] = df['type'].map({'Improvement': 0, 'Bug': 1})
    df['priority'] = df['priority'].map({'Trivial': 1, 'Minor': 1, 'Major': 2, 'Blocker': 2, 'Critical': 2})

    preliminary_encoded_datasets_dir = os.path.join(preliminary_encoded_datasets_dir, file_name)
    df.to_csv(preliminary_encoded_datasets_dir, index=False)


for filename, dataset in datasets:
    encode_priority(dataset, filename + '_prelim_encoded.csv')

