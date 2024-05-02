import json
import tkinter as tk
from tkinter import messagebox

# Initialize the Tkinter application
app = tk.Tk()
app.title("Sample Windows App")

tk.Label(app, text="Input:").grid(row=0, column=0)
input_entry = tk.Entry(app)
input_entry.grid(row=0, column=1)

tk.Label(app, text="Input 2:").grid(row=1, column=0)
input_entry_2 = tk.Entry(app)
input_entry_2.grid(row=1, column=1)
app.mainloop()

confirm_button = tk.Button(app, text="Confirm")
confirm_button.grid(row=3, column=3, columnspan=2)
'''
tk.Label(app, text="Last Name:").grid(row=1, column=0)
last_name_entry = tk.Entry(app)
last_name_entry.grid(row=1, column=1)

tk.Label(app, text="Average Grade:").grid(row=2, column=0)
average_grade_entry = tk.Entry(app)
average_grade_entry.grid(row=2, column=1)

add_button = tk.Button(app, text="Add Student", command=add_student)
add_button.grid(row=3, column=0, columnspan=2)


'''