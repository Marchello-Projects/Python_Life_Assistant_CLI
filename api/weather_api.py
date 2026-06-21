import os
from dotenv import load_dotenv

from api.base_api_client import ApiClient

load_dotenv()

class WeatherApi(ApiClient):
    def __init__(self):
        super().__init__("https://api.openweathermap.org/data/2.5/weather")

        self.__api_key = os.getenv("OPENWEATHER_API_KEY")

        if not self.__api_key:
            raise ValueError("OPENWEATHER_API_KEY not found in .env")
        
    def __get_coordinates(self, city):
        geo_url = "https://api.openweathermap.org/geo/1.0/direct"

        params = {
            "q": city,
            "limit": 1,
            "appid": self.__api_key
        }

        data = self._make_request(geo_url, params=params)

        if not data:
            return None
        
        return {
            "name": data[0]["name"],
            "country": data[0].get("country"),
            "lat": data[0]["lat"],
            "lon": data[0]["lon"]
        }
    
    def get_data(self, city):
        coordinates = self.__get_coordinates(city)

        if coordinates is None:
            return None
        
        params = {
            "lat": coordinates["lat"],
            "lon": coordinates["lon"],
            "appid": self.__api_key,
            "units": "metric",
            "lang": "en"
        }

        data = self._make_request(self._base_url, params)

        if data is None:
            return None

        return {
            "city": coordinates["name"],
            "country": coordinates["country"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "description": data["weather"][0]["description"]
        }