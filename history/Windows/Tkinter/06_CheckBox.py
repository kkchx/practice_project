import tkinter as tk

# Create a function to update the label text
def update_label():
    if var.get()=="Checked":
        result_label.pack_forget()
    else: result_label.pack()

# Create the main window
root = tk.Tk()
root.title("Checkbox Widget Example")

# Create a StringVar to store the checkbox state
var = tk.StringVar()

# Create and customize a Checkbox widget
checkbox = tk.Checkbutton(root, text="Check me!", variable=var, onvalue="Checked", offvalue="Unchecked", command=update_label)
checkbox.pack()

# Create a label to display the selected state
result_label = tk.Label(root, text="Selected: Unchecked", font=("Helvetica", 12))
result_label.pack(pady=10)

root.mainloop()
