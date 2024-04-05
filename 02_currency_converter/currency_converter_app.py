import requests
from secrets import API_KEY

def get_api_key():
    return API_KEY


def get_base_currency():
    while True:
        base_currency = input("Enter base currency: ")
        base_currency_amount = input("How much: ")
        if base_currency and len(base_currency) == 3:
            return base_currency, float(base_currency_amount) if base_currency_amount else 1
        else:
            print("Please enter a valid base currency (3-letter code).")


def get_target_currency():
    while True:
        target_currency = input("Enter target currency: ")
        if target_currency and len(target_currency) == 3:
            return target_currency
        else:
            print("Please enter a valid target currency (3-letter code).")


def get_currency_data(base_currency, api_key):
    url = f'https://open.er-api.com/v6/latest/{base_currency}?apikey={api_key}'
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        currency_data = response.json()
        return currency_data
    else:
        return False


def display_currency_data(currency_data, base_currency_amount, base_currency, target_currency):
    exchange_rates = currency_data['rates']

    if target_currency in exchange_rates:
        target_exchange_rate = exchange_rates[target_currency]
        converted_amount = base_currency_amount * target_exchange_rate
        print(f"\n{base_currency_amount} {base_currency} is {converted_amount} {target_currency}")
    else:
        print(f"\nExchange rate for {target_currency} not available.")


def main():
    api_key = get_api_key()
    while True:
        base_currency, base_currency_amount = get_base_currency()
        target_currency = get_target_currency()
        currency_data = get_currency_data(base_currency, api_key)

        if currency_data:
            display_currency_data(currency_data, base_currency_amount, base_currency, target_currency)
        else:
            print(f"Error: currency '{base_currency}' not found or data unavailable. Please try again.")
            continue

        another_check = input("Check another currency? (y/n): ").lower()
        if another_check != 'y':
            break
main()