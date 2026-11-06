
import requests


api_key = "f986180ab3742d208b2354c8825d0dc3"

city = input("Enter city name: ").strip()

if not city:
    print("Please enter a valid city name!")
    exit()

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

try:

    response = requests.get(url, timeout=10)

    # Check API response
    if response.status_code == 200:

        data = response.json()


        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]


        fahrenheit = (temperature * 9/5) + 32


        print("\n===== WEATHER REPORT =====")
        print("City:", city)
        print("Temperature:", round(temperature, 2), "°C")
        print("Temperature:", round(fahrenheit, 2), "°F")
        print("Humidity:", humidity, "%")
        print("Weather:", condition)
        print("Wind Speed:", wind_speed, "m/s")

    else:
        print("Error: City not found or invalid API key.")
        print("Status Code:", response.status_code)

except requests.exceptions.Timeout:
    print("Error: Request timed out. Try again.")

except requests.exceptions.RequestException:
    print("Error: Please check your internet connection.")
