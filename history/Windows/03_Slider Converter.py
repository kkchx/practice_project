import tkinter as tk

# Function to convert temperature
def convert_temperature(fahrenheit):
    celsius = round((fahrenheit - 32) * 5/9,1)
    result_label.config(text=f"{fahrenheit:.2f}°F is {celsius:.2f}°C")

# Create the main window
window = tk.Tk()
window.title("Temperature Converter")

# Create and pack labels
instruction_label = tk.Label(window, text="Select temperature in Fahrenheit:")
instruction_label.pack()

# Create a slider for temperature input
slider = tk.Scale(window, from_=-50, to=150, orient=tk.HORIZONTAL, length=200, resolution=1, command=lambda val: convert_temperature(float(val)))
slider.pack()

# Create and pack a label to display the result
result_label = tk.Label(window, text="")
result_label.pack()

# Start the Tkinter event loop
window.mainloop()
