import tkinter as tk

# Create a function to update the label text
def update_label():
    result_label.config(text="Selected: " + var.get())

# Create the main window
root = tk.Tk()
root.title("Radiobutton Widget Example")

# Create a StringVar to store the selected option
var = tk.StringVar()

# Create and customize RadioButtons
radio_button1 = tk.Radiobutton(root, text="Option 1", variable=var, value="Option 1", command=update_label)
radio_button2 = tk.Radiobutton(root, text="Option 2", variable=var, value="Option 2", command=update_label)
radio_button3 = tk.Radiobutton(root, text="Option 3", variable=var, value="Option 3", command=update_label)

radio_button1.pack()
radio_button2.pack()
radio_button3.pack()

# Create a label to display the selected option
result_label = tk.Label(root, text="Selected: None", font=("Helvetica", 12))
result_label.pack(pady=10)

root.mainloop()
