import requests
#from datetime import datetime

# Replace 'YOUR_API_KEY' and 'CITY_NAME' with your specific information
api_key = '3891e6aaf51fea205fc9ea2e6d6e62c6'
city_name = 'Bangkok'

# Make a GET request to the weather service API
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    weather_data = response.json()
    print(weather_data)
else:
    print(f"Error: Unable to fetch weather data. Status code: {response.status_code}")


temperature = weather_data['main']['temp']
sunrise_timestamp = weather_data['sys']['sunrise']

print (f'Temperature: {temperature} K')


print(f'Sunrise: {sunrise_timestamp}')

#sunrise_time=datetime.utcfromtimestamp(sunrise_timestamp).strftime('%d-%m-%Y %H:%M:%S')
#print(sunrise_time)
