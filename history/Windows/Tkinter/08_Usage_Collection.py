import tkinter as tk
import json

# Function to display selected interests


def show_interests():
    selected_interests = []
    for interest, var in interests_vars.items():
        if var.get():
            selected_interests.append(interest)
    if not selected_interests:
        selected_interests = ["No interests selected"]
    result_label.config(text="Selected Interests: " + ", ".join(selected_interests))

    user_info = {"name": "", "gender": "", "interests": ""}
    user_info["name"]=name_entry.get()
    user_info["gender"]=gender_var.get()
    interests_text= ", ".join(selected_interests)
    user_info["interests"] = interests_text
    with open("user_info.json", "w") as file:
        json.dump(user_info, file)
# Create the main window
root = tk.Tk()
root.title("User Information")


# Create a frame for user information
info_frame = tk.Frame(root)
info_frame.pack(pady=10)

# Labels and Entries for name and gender
name_label = tk.Label(info_frame, text="Name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(info_frame, width=30)
name_entry.grid(row=0, column=1)

gender_label = tk.Label(info_frame, text="Gender:")
gender_label.grid(row=1, column=0)

gender_var = tk.StringVar()
male_radio = tk.Radiobutton(info_frame, text="Male", variable=gender_var, value="Male")
female_radio = tk.Radiobutton(info_frame, text="Female", variable=gender_var, value="Female")
male_radio.grid(row=1, column=1)
female_radio.grid(row=1, column=2)

# Create a frame for interests
interest_frame = tk.Frame(root)
interest_frame.pack(pady=10)

# Checkboxes for interests
interests_vars = {
    "Reading": tk.BooleanVar(),
    "Traveling": tk.BooleanVar(),
    "Cooking": tk.BooleanVar(),
    "Gardening": tk.BooleanVar()
}

for i, (interest, var) in enumerate(interests_vars.items()):
    chk = tk.Checkbutton(interest_frame, text=interest, variable=var)
    chk.grid(row=i, column=0, sticky="w")

# Button to submit
submit_button = tk.Button(root, text="Submit", command=show_interests)
submit_button.pack(pady=10)

# Label to display selected interests
result_label = tk.Label(root, text="Selected Interests:", font=("Helvetica", 12))
result_label.pack()

root.mainloop()
