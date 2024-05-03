from Classes.CleanData import CleanData
import pandas as pd
from configurations import text_column_to_use as column_to_clean

merged_df = pd.read_csv(r'../datasets/abstracted datasets/merged_abstracted.csv')

cleaner = CleanData()
cleaner.clean_text(merged_df, column_to_clean)

# Save the cleaned data
merged_df.to_csv(r'../datasets/cleaned datasets/merged_cleaned.csv', index=False)
