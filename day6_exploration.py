import pandas as pd
df = pd.read_csv('bag_policies.csv')
print(df.head())
print(df['bag_policy'].value_counts())
print(df['state'].unique())