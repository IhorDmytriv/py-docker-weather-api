import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    response = requests.get(
        "https://api.weatherapi.com/v1/current.json?q=Paris&key=" + API_KEY
    )

    if response.status_code == 200:
        json_data = response.json()

        city_location_data = json_data["location"]
        for key, value in city_location_data.items():
            print(f"{key}: {value}")

        city_weather_data = json_data["current"]
        for key, value in city_weather_data.items():
            print(f"{key}: {value}")
    else:
        print("Error:", response.status_code, response.text)


if __name__ == "__main__":
    get_weather()
