import requests

# OpenWeatherMap API Key (Replace with your own key)
API_KEY = "e372ed703d122d56c786612afee9b8f4"  # Updated with the provided API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather = {
            "City": data["name"],
            "Temperature": f"{data['main']['temp']}°C",
            "Humidity": f"{data['main']['humidity']}%",
            "Condition": data["weather"][0]["description"].capitalize(),
        }
        return weather
    elif response.status_code == 404:
        return "Error: City not found. Please enter a valid city name."
    else:
        return "Error: Unable to fetch weather data."

def main():
    city = input("Enter city name: ")
    weather_data = get_weather(city)
    
    if isinstance(weather_data, dict):
        print("\n--- Current Weather ---")
        for key, value in weather_data.items():
            print(f"{key}: {value}")
    else:
        print(weather_data)

if __name__ == "__main__":
    main()
