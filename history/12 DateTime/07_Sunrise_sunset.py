import requests
from datetime import datetime, timedelta

def get_sunrise_sunset(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        sunrise_timestamp = data['sys']['sunrise']
        sunset_timestamp = data['sys']['sunset']

        # Add 7 hours (UTC+7) to the timestamps
        sunrise_local = datetime.utcfromtimestamp(sunrise_timestamp)# + timedelta(hours=7)
        sunset_local = datetime.utcfromtimestamp(sunset_timestamp)# + timedelta(hours=7)

        return sunrise_local, sunset_local
    else:
        return None

def main():
    api_key = "3891e6aaf51fea205fc9ea2e6d6e62c6"
    city = "Chumphon,th"

    result = get_sunrise_sunset(api_key, city)

    if result:
        sunrise, sunset = result
        print(f"Sunrise in Chumphon: {sunrise.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Sunset in Chumphon: {sunset.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print("Error fetching data. Please check your API key or city name.")

main()