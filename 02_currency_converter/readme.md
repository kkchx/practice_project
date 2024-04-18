# Task: Currency Converter
1. Create a console-based currency converter app, that
   2. Prompts user for a base and target currency, value
   3. Connects to the Currency Server using API and gets a response
   4. Prints the following information: Money in Base and Target Currency
   5. Asks user if he wants to convert more
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

# Replace 'your_api_key' and 'base_currency' with your ExchangeRate-API key and desired base currency
api_key = API_KEY
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

        # Extract and display currency exchange rates from the JSON response
        base_currency = data['base_code']
        exchange_rates = data['rates']

        # Display information
        print(f"Exchange rates for 1 {base_currency}:")
        for currency, rate in exchange_rates.items():
            print(f"{currency}: {rate}")
    else:
        print("Error:", response.status_code)

except requests.ConnectionError:
    print("Failed to connect to the API. Please check your internet connection.")

```

API_KEY = '4850f6377aad21f73f686562'