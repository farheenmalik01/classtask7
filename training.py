import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import mlflow

# Load data
df = pd.read_csv('processed_data.csv')
X = df[['Humidity', 'Wind Speed']].values
y = df['Temperature'].values

# Start MLFlow experiment
mlflow.set_experiment("Weather Prediction")

with mlflow.start_run():
    # Model training
    model = LinearRegression()
    model.fit(X, y)

    # Log parameters and metrics
    mlflow.log_param("model", "LinearRegression")
    mlflow.log_param("features", "Humidity, Wind Speed")
    mlflow.log_metric("r2_score", model.score(X, y))

    # Save and register model
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
    mlflow.log_artifact("model.pkl")

    print("Model training complete. Logged to MLFlow.")
