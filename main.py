import json
import csv
from location import Location

# Take latitude and longitude as float inputs and instantiate location object 
lat = int(input("Enter latitude:"))
lng = int(input("Enter longitude:"))
location = Location(lat, lng)
print(location.get_coordinate())

#Set weather info to be equal to JSON of historical weather
weather_info = location.historical_weather()
weather = weather_info.content # dump content of the file into a weather variable

with open('weather.json', 'wb') as f: # Create and write JSON file called weather and dump content into it
    f.write(weather)

with open('weather.json') as weather_json: #Open data.JSON file and store in weather variable
  weather = json.load(weather_json)

yearly_weather_statistics = weather['result'] # Set yearly weather stats equal to all info underneath the result category

weather_file = open('weather_data.csv', 'w') # Opens the csv file to be written
csv_writer = csv.writer(weather_file) # Creates csv writer set to that specific csv

count = 0
for weather_type in yearly_weather_statistics:
    if count < 1: # Writes the first row of the CSV as headers
        headers = ['day'] # Creates a list od all headers with the first component being day
        for i in range(2, 8): # Each statistic for each type of weather data is collected and written as header
            for statistic in list(weather_type.values())[i]:
                headers.append(f"{list(weather_type.keys())[i]}_" + statistic)
        csv_writer.writerow(headers)
        count += 1 
    else:
        values = list(weather_type.values())
        data_points = [count]
        for value in values:
          if type(value) is dict:
            inner_values = list(value.values())
            for data_point in inner_values:
              data_points.append(data_point)
        csv_writer.writerow(data_points)
    count += 1

weather_file.close() # Closes the weather file

# Repeats the above process but does it with the historical irradiance data
irradiance_info = location.historical_irradiance()
irradiance = irradiance_info.content

with open('irradiance.json', 'wb') as g:
  g.write(irradiance)

with open('irradiance.json') as irradiance_json:
  irradiance = json.load(irradiance_json)

yearly_irradiance_statistics = dict(irradiance['outputs'])

irradiance_file = open('irradiance_data.csv', 'w')
csv_writer = csv.writer(irradiance_file)

csv_writer.writerow(['Months', "Average DNI", "Average GHI", "Average Latitudal Tilt"])

print(yearly_irradiance_statistics)
count = 0
months = list(yearly_irradiance_statistics['avg_dni']['monthly'].keys())
print(months)
irradiance_type_vals = []
avg_dni = []
avg_ghi = []
avg_lat_tilt = []

for irradiance_type in yearly_irradiance_statistics:
    print(type(irradiance_type))
    values = []
    for value in list(yearly_irradiance_statistics[f'{irradiance_type}']['monthly'].values()):
      values.append(value)
    if count == 0:
      avg_dni = values
      count += 1
    elif count == 1:
      avg_ghi = values
      count += 1
    elif count == 2:
      avg_lat_tilt = values


organized_data = list(zip(months, avg_dni, avg_ghi, avg_lat_tilt))
print(organized_data)

for row in organized_data:
  csv_writer.writerow(row)

irradiance_file.close()