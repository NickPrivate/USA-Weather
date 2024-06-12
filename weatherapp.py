# Command Line App using OpenWeatherMap API

import requests
from config import API_KEY, BASE_URL

#User Input
state = input("Enter the name of the State: ")
city = input("Enter the name of the City: ")


params =  {
    'q' : f'{city},{state}',
    'appid' : API_KEY,
    'units': 'imperial'
}

response = requests.get(BASE_URL,params)



if response.status_code == 200:
    weather_data = response.json()
    print(f"Weather in {weather_data['name']}, {weather_data['sys']['country']}:")
    print(f"Temperature: {weather_data['main']['temp']}°F")
    print(f"Description: {weather_data['weather'][0]['description']}")
else:
    print("Error fetching weather data.")

