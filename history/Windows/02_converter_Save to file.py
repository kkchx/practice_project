import tkinter as tk
import json

# Function to convert temperature
def convert_temperature():
    try:
        fahrenheit = float(entry.get())
        celsius = (fahrenheit - 32) * 5/9
        result_label.config(text=f"{fahrenheit}°F is {celsius:.2f}°C")
        temp_info = {"temp_F": "", "temp_C": "", "result": ""}
        temp_info["temp_F"] = entry.get()
        temp_info["temp_C"] = celsius
        temp_info["result"] = str(fahrenheit)+"F is "+str(celsius)+"C"
        with open("temp.json", "w") as file:
            json.dump(temp_info, file)
    except ValueError:
        result_label.config(text="Invalid input")

# Create the main window
window = tk.Tk()
window.title("Temperature Converter")

# Create and pack labels and entry field
instruction_label = tk.Label(window, text="Enter temperature in Fahrenheit:")
instruction_label.pack()

entry = tk.Entry(window)
entry.pack()

# Create and pack a "Convert" button
convert_button = tk.Button(window, text="Convert", command=convert_temperature)
convert_button.pack()

# Create and pack a label to display the result
result_label = tk.Label(window, text="")
result_label.pack()

# Start the Tkinter event loop
window.mainloop()
