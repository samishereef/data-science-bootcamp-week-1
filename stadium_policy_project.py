import pandas as pd
df = pd.read_csv('funding_policy.csv')
print(df['total_cost_millions'].describe())