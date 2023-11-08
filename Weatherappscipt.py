import requests
import json

def get_weather(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric" 
         
          # You can change to "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if response.status_code == 200:
            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"]
            city_name = data["name"]
            country_code = data["sys"]["country"]
            print(f"Weather in {city_name}, {country_code}: {description}")
            print(f"Temperature: {temperature}°C")
        else:
            print(f"Error: {data['message']}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def main():
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    city = input("Enter the city: ")
    get_weather(api_key, city)

if __name__ == "__main__":
    main()