import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Function to update the OptionMenu based on Combobox selection
def update_option_menu(event):
    selected_greeting = selected_greeting_var.get()
    selected_greeting_var_optionmenu.set(selected_greeting)

# Function to show a message box
def show_message():
    selected_greeting = selected_greeting_var.get()
    message = f"Selected Greeting: {selected_greeting}"
    messagebox.showinfo("Selected Greeting", message)

# Create the main window
root = tk.Tk()
root.title("Symmetric Combobox and OptionMenu Demo")

# Create a Frame for the left side
left_frame = tk.Frame(root)
left_frame.pack(side="left", padx=10)

# Create a Label for the Combobox
greeting_label_combobox = tk.Label(left_frame, text="Select a Greeting (Combobox):")
greeting_label_combobox.pack(pady=10)

# Create a Combobox
selected_greeting_var = tk.StringVar()
greeting_combobox = ttk.Combobox(left_frame, textvariable=selected_greeting_var)
greeting_combobox['values'] = ("Hello", "Good Morning", "Good Evening")
greeting_combobox.set("Hello")
greeting_combobox.pack()

# Bind the update_option_menu function to the Combobox selection event
greeting_combobox.bind("<<ComboboxSelected>>", update_option_menu)

# Create a Button to show the selected greeting
show_message_button_left = tk.Button(left_frame, text="Show Greeting", command=show_message)
show_message_button_left.pack(pady=10)

# Create a Frame for the right side
right_frame = tk.Frame(root)
right_frame.pack(side="right", padx=10)

# Create a Label for the OptionMenu
greeting_label_optionmenu = tk.Label(right_frame, text="Select a Greeting (OptionMenu):")
greeting_label_optionmenu.pack()

# Create an OptionMenu
selected_greeting_var_optionmenu = tk.StringVar()
greeting_options = ["Hello", "Good Morning", "Good Evening"]
greeting_optionmenu = tk.OptionMenu(right_frame, selected_greeting_var_optionmenu, *greeting_options)
greeting_optionmenu.pack()

# Set the initial value of the OptionMenu to match the Combobox
selected_greeting_var_optionmenu.set(selected_greeting_var.get())

# Create a Button to show the selected greeting
show_message_button_right = tk.Button(right_frame, text="Show Greeting", command=show_message)
show_message_button_right.pack(pady=10)

root.mainloop()
