import json
import tkinter as tk
from tkinter import messagebox

# Initialize the Tkinter application
app = tk.Tk()
app.title("Student Record Management")

# Define an empty list to store student records
students = []

# Function to add a student record
def add_student():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    average_grade = average_grade_entry.get()

    try:
        average_grade = float(average_grade)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid numeric grade.")
        return

    student = {
        "first_name": first_name,
        "last_name": last_name,
        "average_grade": average_grade
    }

    students.append(student)
    save_to_file()
    clear_entries()
    messagebox.showinfo("Success", "Student record added successfully.")

# Function to delete a student record
def delete_student():
    if students:
        try:
            index = int(delete_index_entry.get()) - 1
            if 0 <= index < len(students):
                del students[index]
                save_to_file()
                delete_index_entry.delete(0, tk.END)
                messagebox.showinfo("Success", "Student record deleted successfully.")
            else:
                messagebox.showerror("Error", "Invalid student number.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid numeric index.")
    else:
        messagebox.showinfo("Info", "No student records to delete.")

# Function to print all student records
def print_all_records():
    if students:
        output_text.delete(1.0, tk.END)
        for i, student in enumerate(students):
            output_text.insert(tk.END, f"{i+1}. {student['first_name']} {student['last_name']}, Average Grade: {student['average_grade']}\n")
    else:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "No student records available.")

# Function to sort student records by grade (ascending)
def sort_records_ascending():
    if students:
        sorted_students = sorted(students, key=lambda x: x['average_grade'])
        print_sorted_records(sorted_students)
    else:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "No student records available.")

# Function to sort student records by grade (descending)
def sort_records_descending():
    if students:
        sorted_students = sorted(students, key=lambda x: x['average_grade'], reverse=True)
        print_sorted_records(sorted_students)
    else:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "No student records available.")

# Function to print sorted records
def print_sorted_records(sorted_students):
    output_text.delete(1.0, tk.END)
    for i, student in enumerate(sorted_students):
        output_text.insert(tk.END, f"{i+1}. {student['first_name']} {student['last_name']}, Average Grade: {student['average_grade']}\n")

# Function to save the collection to a local file
def save_to_file():
    with open("../Student Management/student_records.json", "w") as file:
        json.dump(students, file)

# Function to clear input entries
def clear_entries():
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    average_grade_entry.delete(0, tk.END)

# Create and configure GUI elements
tk.Label(app, text="First Name:").grid(row=0, column=0)
first_name_entry = tk.Entry(app)
first_name_entry.grid(row=0, column=1)

tk.Label(app, text="Last Name:").grid(row=1, column=0)
last_name_entry = tk.Entry(app)
last_name_entry.grid(row=1, column=1)

tk.Label(app, text="Average Grade:").grid(row=2, column=0)
average_grade_entry = tk.Entry(app)
average_grade_entry.grid(row=2, column=1)

add_button = tk.Button(app, text="Add Student", command=add_student)
add_button.grid(row=3, column=0, columnspan=2)

tk.Label(app, text="Enter Index to Delete:").grid(row=4, column=0)
delete_index_entry = tk.Entry(app)
delete_index_entry.grid(row=4, column=1)

delete_button = tk.Button(app, text="Delete Student", command=delete_student)
delete_button.grid(row=5, column=0, columnspan=2)

print_button = tk.Button(app, text="Print All Records", command=print_all_records)
print_button.grid(row=6, column=0, columnspan=2)

sort_asc_button = tk.Button(app, text="Sort Records (Ascending)", command=sort_records_ascending)
sort_asc_button.grid(row=7, column=0, columnspan=2)

sort_desc_button = tk.Button(app, text="Sort Records (Descending)", command=sort_records_descending)
sort_desc_button.grid(row=8, column=0, columnspan=2)

output_text = tk.Text(app, height=10, width=40)
output_text.grid(row=9, column=0, columnspan=2)

# Load existing student records from the file if it exists
try:
    with open("../Student Management/student_records.json", "r") as file:
        students = json.load(file)
except FileNotFoundError:
    pass

# Start the Tkinter main loop
app.mainloop()
