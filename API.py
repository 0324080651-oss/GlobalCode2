from  pprint import pprint
import requests
r = "https://api.open-meteo.com/v1/forecast?latitude=5.6037&longitude=-0.1870&current=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m"

pprint(r.json) 