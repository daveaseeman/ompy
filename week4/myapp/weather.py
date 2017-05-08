# -*- coding: utf-8 -*-
import os
import forecastio
from geopy.geocoders import Nominatim

# Only used when running locally
# from dotenv import load_dotenv, find_dotenv
# load_dotenv(find_dotenv())


def get_forecast(address):
    lat_and_long = get_lat_long(address)
    lat = lat_and_long[0]
    lng = lat_and_long[1]
    forecast_key = os.environ['API_KEY']
    forecast = forecastio.load_forecast(forecast_key, lat, lng)
    current_forecast = forecast.currently()
    current_condition = current_forecast.icon
    current_temperature = current_forecast.temperature
    current_wind = current_forecast.windSpeed
    current_bearing = get_direction(current_forecast.windBearing)
    current_visibility = current_forecast.visibility
    forecast = "Currently {} and {}°F, wind {} at {}mph , visibility {} miles at {}".format(
        current_condition.lower(),
        current_temperature,
        current_bearing,
        current_wind,
        current_visibility,
        address
    )
    return forecast


def get_map(address):
    lat_and_long = get_lat_long(address)
    lat = str(lat_and_long[0])
    lng = str(lat_and_long[1])
    map_key = os.environ['GOOGLE_MAP_API_KEY']
    map_base_url = "https://www.google.com/maps/embed/v1/view?key="
    map_location = "&center=" + lat + "," + lng
    map_params = "&zoom=14&maptype=satellite"
    map_insert = map_base_url + map_key + map_location + map_params
    return map_insert


def get_lat_long(address):
    geolocator = Nominatim()
    location = geolocator.geocode(address)
    lat = location.latitude
    lng = location.longitude
    lat_lng = [lat, lng]
    return lat_lng


def get_direction(num):
    val = int((num / 22.5) + .5)
    arr = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    direction = arr[(val % 16)]
    return direction
