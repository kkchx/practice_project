import tkinter as tk

# Create a function to handle button click
def submit():
    user_input = entry.get()  # Get the text from the Entry widget
    result_label.config(text="You entered: " + user_input)

def clear():
    entry.delete(0,'end')

# Create the main window
root = tk.Tk()
root.title("Entry Widget Example")

# Create and customize an Entry widget
entry = tk.Entry(root, width=30, font=("Helvetica", 12))
entry.insert(0, "Type something here")  # Pre-fill with default text
entry.pack(pady=10)

# Create a button to submit the text from the Entry widget
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

root.mainloop()
