
import requests
import os

api_key = os.getenv("OPENWEATHER_API_KEY")

if not api_key:
    print("API key is missing! Please set your API key.")
    exit()


city = input("Enter city name: ").strip()

if not city:
    print("Please enter a valid city name!")
    exit()


url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": api_key,
    "units": "metric"
}

try:
    response = requests.get(url, params=params, timeout=10)

    if response.status_code == 200:

        data = response.json()

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        fahrenheit = (temperature * 9 / 5) + 32

        print("\n===== WEATHER REPORT =====")
        print("City:", data["name"])
        print("Temperature:", round(temperature, 2), "°C")
        print("Temperature:", round(fahrenheit, 2), "°F")
        print("Humidity:", humidity, "%")
        print("Weather:", condition)
        print("Wind Speed:", wind_speed, "m/s")

    elif response.status_code == 404:
        print("Error: City not found!")

    elif response.status_code == 401:
        print("Error: Invalid API key!")

    else:
        print("Something went wrong!")
        print("Status Code:", response.status_code)

except requests.exceptions.Timeout:
    print("Error: Request timed out. Try again.")

except requests.exceptions.RequestException:
    print("Error: Please check your internet connection.")

