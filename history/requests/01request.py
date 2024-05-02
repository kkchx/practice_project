import requests
while True:
    print("Please enter a number of todo... to exit type 0")
    user_input = str(input("enter a number: "))
    api_url = "https://jsonplaceholder.typicode.com/todos/" # Example API URL
    api_url2 = api_url + user_input
    # Check if the request was successful (status code [200])
    response = requests.get(api_url2)
    if response.status_code == 200:
        data = response.json()
        print("Title:", data.get("title"))
        print("Completed:", data.get("completed"))
    else:
        print("Error:", response.status_code)