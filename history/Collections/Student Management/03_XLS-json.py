'''
pip install pandas (Terminal AltF2)

'''

import pandas as pd
import json

try:
    # Load the Excel file into a pandas DataFrame
    excel_file = "List.xlsx"  # Replace with your Excel file path
    df = pd.read_excel(excel_file)

    # Convert the DataFrame to a dictionary
    data_dict = df.to_dict(orient="records")

    # Define the JSON output file path
    json_file = "output.json"

    # Write the dictionary to a JSON file
    with open(json_file, "w") as f:
        json.dump(data_dict, f, indent=4)

    print(f"Excel table converted and saved as {json_file}")
except FileNotFoundError:
    print("Error: The Excel file does not exist. Please provide a valid file path.")
except Exception as e:
    print(f"An error occurred: {e}")
