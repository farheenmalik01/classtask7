import pandas as pd

df = pd.read_csv('raw_data.csv')

# Handle missing values
df.fillna(method='ffill', inplace=True)

# Normalize numerical fields
df['Temperature'] = (df['Temperature'] - df['Temperature'].mean()) / df['Temperature'].std()
df['Wind Speed'] = (df['Wind Speed'] - df['Wind Speed'].mean()) / df['Wind Speed'].std()

df.to_csv('processed_data.csv', index=False)
print("Data preprocessing complete. Saved to processed_data.csv")
