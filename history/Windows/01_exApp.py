import tkinter as tk
from tkinter import ttk


# Function to handle button click and display output in the same window
def on_button_click():
    input1_value = input1.get()
    input2_value = input2.get()
    dropdown_value = dropdown_var.get()

    # Create a label to display the output
    output_label.config(text=f"Input 1: {input1_value}\nInput 2: {input2_value}\nSelected Option: {dropdown_value}")


# Create the main application window
root = tk.Tk()
root.title("Windows App with Inputs and Dropdown")

# Input fields
input1_label = tk.Label(root, text="Input 1:")
input1_label.pack()
input1 = tk.Entry(root)
input1.pack()

input2_label = tk.Label(root, text="Input 2:")
input2_label.pack()
input2 = tk.Entry(root)
input2.pack()

# Dropdown menu
dropdown_label = tk.Label(root, text="Select an option:")
dropdown_label.pack()

options = ["Option 1", "Option 2", "Option 3"]
dropdown_var = tk.StringVar()
dropdown = ttk.Combobox(root, textvariable=dropdown_var, values=options)
dropdown.pack()

# Button
button = tk.Button(root, text="Submit", command=on_button_click)
button.pack()

# Label to display output
output_label = tk.Label(root, text="")
output_label.pack()

# Start the main event loop
root.mainloop()
