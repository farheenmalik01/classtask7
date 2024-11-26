import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv('processed_data.csv')
X = df[['Humidity', 'Wind Speed']].values
y = df['Temperature'].values

model = LinearRegression()
model.fit(X, y)

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model training complete. Saved to model.pkl")
