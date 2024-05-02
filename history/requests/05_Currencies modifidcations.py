"""
modify the code to show only AED, JPY and THB
"""

import requests

# Replace 'your_api_key' and 'base_currency' with your ExchangeRate-API key and desired base currency
api_key = '4850f6377aad21f73f686562'
base_currency = 'USD'  # Replace with the desired base currency code

# Set up query parameters
params = {
    'apikey': api_key,
    'base': base_currency
}

try:
    # Make a GET request to fetch exchange rates
    response = requests.get("https://open.er-api.com/v6/latest", params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()

        # Extract and display specific currency exchange rates from the JSON response
        base_currency = data['base_code']
        exchange_rates = data['rates']

        # Display information for AED, THB, and JPY
        print(f"Exchange rates for 1 {base_currency} to specific currencies:")
        for currency in ['AED', 'THB', 'JPY']:
            rate = exchange_rates.get(currency)
            if rate is not None:
                print(f"{currency}: {rate}")
            else:
                print(f"{currency}: Exchange rate not available")

    else:
        print("Error:", response.status_code)

except requests.ConnectionError:
    print("Failed to connect to the API. Please check your internet connection.")
