# Task: Weather Forecast
1. Create a console-based weather app, that
   2. Prompts user for a city (use error-proofing) to check weather
   3. Connects to the Weather Server using API and gets a response
   4. Prints the following information: City, Country, Temp in C, Feels like, Cloud Conditions, Humidity, Altitude
   5. Asks user if he wants to check another city or exit a program (use a loop)
2. Create a proper documentation in readme1.md
3. Do self code-review and wait for Collaborator to review before merging to Main/Master Branch
4. Remember, we're creating a show-case, so use best practices from all previous projects
   
## as an example, use a code from previous projects
change the logic to use functions to guarantee:
1. Correct input
2. Request, and handling of a non-200 response
3. Output
4. Iteration of the main loop

```python

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


```
