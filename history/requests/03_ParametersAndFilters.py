import requests

def get_weather_data(api_key, city, country):
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # Set up query parameters
    params = {
        'q': f"{city},{country}",
        'appid': api_key
    }

    try:
        response = requests.get(base_url, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()

            # Display relevant weather information
            print(f"Weather in {city}, {country}:")
            print("Temperature:", data['main']['temp'], "K")
            print("Description:", data['weather'][0]['description'])
            print("Humidity:", data['main']['humidity'])
            print("Wind Speed:", data['wind']['speed'])
        else:
            print("Error:", response.status_code)

    except requests.ConnectionError:
        print("Failed to connect to the API. Please check your internet connection.")


#https://www.iso.org/iso-3166-country-codes.htmley, city, and country
api_key = '3891e6aaf51fea205fc9ea2e6d6e62c6'
city_name = 'Bangkok'
country_code = 'TH'
get_weather_data(api_key, city_name, country_code)
