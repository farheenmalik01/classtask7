import React, { useState } from 'react';

const WeatherForm = () => {
    const [humidity, setHumidity] = useState('');
    const [windSpeed, setWindSpeed] = useState('');
    const [temperature, setTemperature] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await fetch("http://localhost:8000/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ humidity, wind_speed: windSpeed })
        });
        const data = await response.json();
        setTemperature(data.temperature);
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input type="number" placeholder="Humidity" value={humidity} onChange={e => setHumidity(e.target.value)} />
                <input type="number" placeholder="Wind Speed" value={windSpeed} onChange={e => setWindSpeed(e.target.value)} />
                <button type="submit">Predict</button>
            </form>
            {temperature && <p>Predicted Temperature: {temperature}</p>}
        </div>
    );
};

export default WeatherForm;
