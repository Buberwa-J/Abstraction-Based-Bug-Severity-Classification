import pandas as pd
from configurations import text_column_to_use as column_to_abstract
from Classes.AbstractionMapping import AbstractionMapping
from source.Classes.Pattern import Pattern
from Classes.AbstractDetail import AbstractDetail

merged_df = pd.read_csv(r'../datasets/merged datasets/merged_df.csv')

pattern = Pattern()
abstraction_mapping = AbstractionMapping()

# Create instances of AbstractDetail
abstractor = AbstractDetail(pattern=pattern, abstraction_mapping=abstraction_mapping)

# Abstract the chosen column in the dataframes
abstractor.abstract_text(merged_df, column_to_abstract)

# Save the dataframe after abstraction
merged_df.to_csv(r'../datasets/abstracted datasets/merged_abstracted.csv', index=False)

