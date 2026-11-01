import httpx
import json
from models.model import WeatherResponseModel
from config.config import WEATHER_API_KEY
from services.cache import get_from_cache, set_in_cache



async def get_weather(destination: str, start_date: str, end_date: str)-> list[WeatherResponseModel]:
    """Fetch weather data for the given destination and date range"""
    # Here you would typically call the weather API using the WEATHER_API_KEY
    # For now, we'll return a placeholder response

    cache_key = f"{destination}_{start_date}_{end_date}"

    cached_data = get_from_cache(cache_key)
    if cached_data:
        return cached_data

    async with httpx.AsyncClient() as client:
      response = await client.get("https://api.weatherapi.com/v1/forecast.json", params={
          "q": destination,
          "dt": start_date,
          "end_dt": end_date,
          "key": WEATHER_API_KEY
      })
      response.raise_for_status()
      data = response.json()
      print(json.dumps(data))
    
      forecasts = []
      for day in data['forecast']['forecastday']:
          forecast = WeatherResponseModel(
              date=day['date'],
              condition=day['day']['condition']['text'],
              temperature_high=day['day']['maxtemp_c'],
              temperature_low=day['day']['mintemp_c'],
              humidity=day['day']['avghumidity'],
              rain_chance=day['day']['daily_chance_of_rain']
          )
          forecasts.append(forecast)
      set_in_cache(cache_key, forecasts, ttl=3600)
      return forecasts