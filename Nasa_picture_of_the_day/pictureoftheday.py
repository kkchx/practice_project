import requests

def get_apod(api_key, date):
    base_url = "https://api.nasa.gov/planetary/apod"

    # Set up query parameters
    params = {
        'api_key': api_key,
        'date': date
    }

    try:
        response = requests.get(base_url, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()

            # Handle JSON response
            display_apod_info(data)

            #download_and_save_image(data['url'], f"apod_{date}.jpg")
        else:
            print("Error:", response.status_code)

    except requests.ConnectionError:
        print("Failed to connect to the API. Please check your internet connection.")

def display_apod_info(data):
    # Extract and display information from the APOD JSON response
    date = data['date']
    title = data['title']
    explanation = data['explanation']
    url = data['url']

    # Display information
    print(f"Astronomy Picture of the Day ({date}):")
    print("Title:", title)
    print("Explanation:", explanation)
    print("URL:", url)


# Replace 'your_api_key' with your NASA APOD API key
api_key = 'DEMO_KEY'

# Get user input for the desired date
user_date = input("Enter a date (YYYY-MM-DD) to see the Astronomy Picture of the Day: ")

get_apod(api_key, user_date)
