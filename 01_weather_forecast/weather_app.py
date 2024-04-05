import requests
from secrets import API_KEY

def gets_api_key():
    # Replace with your actual API key
    return API_KEY

def get_city_name():
    while True:
        city = input("Enter a city name to check the weather: ")
        if city:
            if len(city) > 2:
                return city
        else:
            print("Please enter a valid city name.")

def get_weather_data(city_name, api_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        weather_data = response.json()
        return weather_data
    else:
        return False

def display_weather_data(weather_data):
    City = weather_data['name']
    Country = weather_data['sys']['country']
    Temperature = weather_data['main']['temp']
    Feels_like = weather_data['main']['feels_like']
    Cloud_Conditions = weather_data['weather'][0]['description']
    Humidity = weather_data['main']['humidity']
    try:
        Altitude = weather_data['main']['sea_level']
    except KeyError:
        Altitude = "Not available"
    print(f"\nCity: {City}, {Country}")
    print(f"Temperature: {Temperature} C")
    print(f"Feels like: {Feels_like} C")
    print(f"Cloud Conditions: {Cloud_Conditions}")
    print(f"Humidity: {Humidity}")
    print(f"Altitude: {Altitude}")
def main():
    api_key = gets_api_key()
    while True:
        city_name = get_city_name()
        weather_data = get_weather_data(city_name, api_key)

        if weather_data:
            display_weather_data(weather_data)
        else:
            print(f"Error: city '{city_name}' not found or data unavailable. Please try again.")
            continue

        another_check = input("Check another city? (y/n): ").lower()
        if another_check != 'y':
            break

main()