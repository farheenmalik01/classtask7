import requests
import pandas as pd
from datetime import datetime

API_KEY = '46480b0708eb3b443c8e6a6eee371ec7'
CITY = 'London'
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

weather_data = []
for entry in data['list']:
    weather_data.append({
        'Date': entry['dt_txt'],
        'Temperature': entry['main']['temp'],
        'Humidity': entry['main']['humidity'],
        'Wind Speed': entry['wind']['speed'],
        'Weather Condition': entry['weather'][0]['description']
    })

df = pd.DataFrame(weather_data)
df.to_csv('raw_data.csv', index=False)
print("Data saved to raw_data.csv")

