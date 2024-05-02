import requests
def fetch_data(record_nu):
    api_url = "https://jsonplaceholder.typicode.com/todos/" + str(record_nu)
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        print("Title:", data.get("title"))
        print("Completed:", data.get("completed"))
    else:
        print("Error:", response.status_code)


while True:
    user_input = input("Please enter a number of todo... to exit type 0\n")
    if user_input=='0':
        break
    else:
        for i in range(1, int(user_input)+1):
            fetch_data(i)

