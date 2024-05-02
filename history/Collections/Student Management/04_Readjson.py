import json



# Define the JSON file path
json_file = "output.json"  # Replace with your JSON file path

try:
    # Read the JSON file into a dictionary
    with open(json_file, "r") as f:
        data_dict = json.load(f)

    # Print the dictionary
    print("Contents of the JSON file as a dictionary:")
    print(data_dict)
except FileNotFoundError:
    print(f"Error: The JSON file '{json_file}' does not exist.")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
