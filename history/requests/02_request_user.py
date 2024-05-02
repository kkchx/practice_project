'''
Enable user to enter a number of todo to request from server
'''
import requests


def fetch_data_from_api(number):
    api_url = "https://jsonplaceholder.typicode.com/todos/" + str(number)  # Example API URL

    try:
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            print("Title:", data.get("title"))
            print("Completed:", data.get("completed"))
        else:
            print("Error:", response.status_code)

    except requests.ConnectionError:
        print("Failed to connect to the API. Please check your internet connection.")


while True:
    number = input("Please enter a number of todo... To exit type 0\n")
    if number == '0':
        break
    else:
        fetch_data_from_api(number)
