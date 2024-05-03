import pandas as pd

ambari = pd.read_csv('../datasets/preliminary encoded datasets/ambari_prelim_encoded.csv')
camel = pd.read_csv('../datasets/preliminary encoded datasets/camel_prelim_encoded.csv')
derby = pd.read_csv('../datasets/preliminary encoded datasets/derby_prelim_encoded.csv')
wicket = pd.read_csv('../datasets/preliminary encoded datasets/wicket_prelim_encoded.csv')

merged_df = pd.concat([ambari, camel, derby, wicket], ignore_index=True)

merged_df.to_csv(r"..\datasets\merged datasets\merged_df.csv", index=False)
