# -*- coding: utf-8 -*-
import os
import forecastio
from geopy.geocoders import Nominatim

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

api_key = os.environ['API_KEY']
address = "Radnor Lake, TN"


def get_weather(address, api_key):
    geolocator = Nominatim()
    location = geolocator.geocode(address)
    lat = location.latitude
    lng = location.longitude
    forecast = forecastio.load_forecast(api_key, lat, lng)
    current_forecast = forecast.currently()
    current_summary = current_forecast.summary
    current_temperature = current_forecast.temperature
    weather_report = "{} and {}° at {}".format(
        current_summary,
        current_temperature,
        address
    )
    return weather_report


print(get_weather(address, api_key))
