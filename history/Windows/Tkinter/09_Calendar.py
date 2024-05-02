import tkinter as tk
import calendar

def show_calendar(year, month):
    cal_text.config(text=calendar.month(year, month))

def prev_month():
    global current_year, current_month
    current_month -= 1
    if current_month == 0:
        current_month = 12
        current_year -= 1
    show_calendar(current_year, current_month)

def next_month():
    global current_year, current_month
    current_month += 1
    if current_month == 13:
        current_month = 1
        current_year += 1
    show_calendar(current_year, current_month)

# Initialize the current year and month
current_year = 2023
current_month = 10

# Create the main window
root = tk.Tk()
root.title("Calendar Display")

# Create a frame for the calendar
calendar_frame = tk.Frame(root)
calendar_frame.pack()

# Create labels for navigation
prev_button = tk.Button(calendar_frame, text="Prev", command=prev_month)
prev_button.grid(row=0, column=0)
next_button = tk.Button(calendar_frame, text="Next", command=next_month)
next_button.grid(row=0, column=6)

# Create a label to display the calendar
cal_text = tk.Label(calendar_frame, text="", font=("Helvetica", 12), justify="left")
cal_text.grid(row=1, column=0, columnspan=7)

# Display the calendar for the current year and month
show_calendar(current_year, current_month)

root.mainloop()
