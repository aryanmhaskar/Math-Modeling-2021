import requests

# Keys stored as constants for convenience
STORMGLASS_API_KEY = "d759c9c6-40c4-11ec-a2d8-0242ac130002-d759ca3e-40c4-11ec-a2d8-0242ac130002"
OPENWEATHER_API_KEY = "15ab2072a6638e83ac39dbd7fe0285e6"
NREL_API_KEY = "SjVZbjGU57N57QRpkS6zbweZZfHF6EYs7YPiVPos"

class Location:
  def __init__(self, lat, lng): # Every location is just a latitude and longitude point
    self.lat = lat
    self.lng = lng

  def get_coordinate(self): # Simple getter, fetches coordinate point of the given value
    return f"{self.lat},{self.lng}"

  def historical_weather(self): # Uses Open Weather data API to fetch general weather information each day in the past year.
    response = requests.get(f"http://history.openweathermap.org/data/2.5/aggregated/year?lat={self.lat}&lon={self.lng}&appid={OPENWEATHER_API_KEY}")
    return response # Response includes cloud coverage, temperature, pressure, wind, humidity, precipitation.

  def historical_irradiance(self): # Uses NREL data API to fetch irradiance monthly averages for past year.
    response = requests.get(f"https://developer.nrel.gov/api/solar/solar_resource/v1.json?api_key={NREL_API_KEY}&lat={int(self.lat)}&lon={int(self.lng)}")
    return response # Response is only irradiance