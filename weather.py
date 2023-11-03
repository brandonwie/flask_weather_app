import os
import requests
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

def get_current_weather(city: str = 'Seoul'):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("OPEN_WEATHER_API_KEY")}&units=metric'

    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == '__main__':
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name: ")

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)