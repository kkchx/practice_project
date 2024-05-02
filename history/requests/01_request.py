import requests

def fetch_data_from_api():
    api_url = "https://jsonplaceholder.typicode.com/todos/1"  # Example API URL

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


fetch_data_from_api()
