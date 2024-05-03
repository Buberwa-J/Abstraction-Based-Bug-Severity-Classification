import pandas as pd
import os
from configurations import text_column_to_use

"""
Dataset Trimming Script

This script reads original datasets from CSV files, selects relevant columns, handles missing values,
and saves trimmed datasets.

Attributes:
    ambari_df (DataFrame): DataFrame containing data from the Ambari dataset.
    camel_df (DataFrame): DataFrame containing data from the Camel dataset.
    derby_df (DataFrame): DataFrame containing data from the Derby dataset.
    wicket_df (DataFrame): DataFrame containing data from the Wicket dataset.
    text_column_to_use (str): Name of the column containing textual data to keep.
    columns_to_keep (list): List of column names to keep in the trimmed datasets.
    datasets (list): List of trimmed DataFrames.
    trimmed_datasets_dir (str): Directory path to save trimmed datasets.
"""


# Read original datasets
ambari_df = pd.read_csv('../datasets/original datasets/Ambari.csv')
camel_df = pd.read_csv('../datasets/original datasets/Camel.csv')
derby_df = pd.read_csv('../datasets/original datasets/Derby.csv')
wicket_df = pd.read_csv('../datasets/original datasets/Wicket.csv')

# Columns to keep, selecting relevant columns
columns_to_keep = ['type', 'priority', text_column_to_use]

# Select relevant columns from each dataset
ambari = ambari_df[columns_to_keep]
camel = camel_df[columns_to_keep]
derby = derby_df[columns_to_keep]
wicket = wicket_df[columns_to_keep]

# Handle missing values
datasets = [ambari, camel, derby, wicket]
for dataset in datasets:
    dataset.dropna(axis=0, how='any', inplace=True)

# Define directory to save trimmed datasets
trimmed_datasets_dir = '../datasets/trimmed datasets/'

# Save trimmed datasets
for df, filename in zip(datasets, ['ambari.csv', 'camel.csv', 'derby.csv', 'wicket.csv']):
    trimmed_filepath = os.path.join(trimmed_datasets_dir, filename)
    df.to_csv(trimmed_filepath, index=False)
