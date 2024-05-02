import json
import tkinter as tk
selected_interests = []
#Function to display selected interests
def user_input():
    selected_interests2 = {
        "Name": name_var,
        "Gender": gender_var,
        "Interests": interest_vars
    }
    selected_interests.append(selected_interests2)
def selected_interests4():
    selected_interests3 = []
    for interest, var in interest_vars.items():
        if var.get():
            selected_interests3.append(interest)
            selected_interests3[interest_vars] = selected_interests3
    #if not selected_interests:
        #selected_interests = ["No interests selected"]
    #result_label.config(text="Selected Interests: " + ",".join(selected_interests3)
def choices(gender):
    if gender_var.get() == "Male":
        gender = "Male"
    elif gender_var.get() == "Female":
        gender = "Female"
def save_to_file():
    with open("User_records.json","w") as file:
        json.dump(selected_interests,file)
'''try:  #if file not found
    with open("User_records.json", "r") as file:  #correct file closure
    selected_interests = json.load(file)
   except FileNotFoundError:
   print("file is not found")
   pass'''
window = tk.Tk()
window.title("User Information")

#Create a frame for user information
info_frame = tk.Frame(window)

name_label = tk.Label(info_frame, text="Name:")
name_label.grid(row=0,column=0)
name_entry = tk.Entry(info_frame, width=30)
name_entry.grid(row=0,column=1)
name_var = name_entry

#Button for submit
submit_button = tk.Button(info_frame, text="Submit",command=save_to_file)
submit_button.grid(row=0,column=2)

gender_label = tk.Label(info_frame, text="Gender:")
gender_label.grid(row=1,column=0)
gender_var = tk.StringVar()
gender = "gender"
male_radio = tk.Radiobutton(info_frame, text="Male", variable=gender_var, value="Male",command=choices("Male"))
female_radio = tk.Radiobutton(info_frame, text="Female",variable=gender_var, value="Female",command=choices("Female"))
male_radio.grid(row=1,column=1)
female_radio.grid(row=1,column=2)
#Create a frame for interests
interest_frame = tk.Frame(window)
#Checkboxes for interests
interest_vars = {
    "Reading": tk.BooleanVar(),
    "Traveling":tk.BooleanVar(),
    "Cooking":tk.BooleanVar(),
    "Gardening":tk.BooleanVar()
}
for i, (interest,var) in enumerate(interest_vars.items()):
    chk = tk.Checkbutton(interest_frame, text=interest, variable=var, command=user_input) #
    chk.grid(row=i, column=0, sticky="w")
#Label to display selected interests
#result_label = tk.Label(window,text="Selected Interests:", font=("Helvetica",12))
info_frame.pack(pady=10)
interest_frame.pack(pady=10)
#result_label.pack()
window.mainloop()
# make a function to when submit put it in a file and print(name: text gender: text, interests: text