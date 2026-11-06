# 🌦️ Basic Weather App

## 📌 Project Description
The Basic Weather App is a Python-based application that fetches real-time weather information for a user-specified city using the OpenWeatherMap API.

## 🛠️ Technologies Used
- Python
- Requests Library
- JSON
- OpenWeatherMap API

## ✨ Features
- Enter any city name to check its weather.
- Displays temperature in Celsius (°C).
- Displays temperature in Fahrenheit (°F).
- Shows humidity percentage.
- Displays weather condition (e.g., light rain, cloudy).
- Shows wind speed.
- Handles invalid city names.
- Handles network errors and request timeouts.
- Validates empty city input.

## ⚙️ Installation

1. Install Python.
2. Install the required library:

```bash
pip install requests
```

3. Get a free API key from OpenWeatherMap:
   https://openweathermap.org/api

4. Add your API key to the Python code:

```python
api_key = "YOUR_API_KEY"
```

5. Run the application:

```bash
python weather.py
```

## 📷 Sample Output

```text
===== WEATHER REPORT =====
City: Tenkasi
Temperature: 26.61 °C
Temperature: 79.9 °F
Humidity: 82 %
Weather: light rain
Wind Speed: 1.19 m/s
```

*Note: Weather values change according to real-time conditions.*

## 👩‍💻 Developed By
**Akshaya**

## 📄 License
This project is created for educational and internship purposes.