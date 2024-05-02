import json

# Define an empty list to store student records
students = []

# Function to add a student record
def add_student():
    first_name = input("Enter the student's first name: ")
    last_name = input("Enter the student's last name: ")
    average_grade = float(input("Enter the student's average grade: "))

    student = {
        "first_name": first_name,
        "last_name": last_name,
        "average_grade": average_grade
    }

    students.append(student)
    save_to_file()

# Function to delete a student record
def delete_student():
    if students:
        print("Current student records:")
        for i, student in enumerate(students):
            print(f"{i+1}. {student['first_name']} {student['last_name']}")

        try:
            index = int(input("Enter the number of the student you want to delete: ")) - 1
            if 0 <= index < len(students):
                del students[index]
                print("Student record deleted.")
                save_to_file()
            else:
                print("Invalid student number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("No student records to delete.")

# Function to print all student records
def print_all_records():
    if students:
        print("Student Records:")
        for i, student in enumerate(students):
            print(f"{i+1}. {student['first_name']} {student['last_name']}, Average Grade: {student['average_grade']}")
    else:
        print("No student records available.")

# Function to sort student records by grade (lowest to highest)
def sort_records_by_grade():
    if students:
        sorted_students = sorted(students, key=lambda x: x['average_grade'], reverse=True)
        print("Student Records Sorted by Average Grade (Lowest to Highest):")
        for i, student in enumerate(sorted_students):
            print(f"{i+1}. {student['first_name']} {student['last_name']}, Average Grade: {student['average_grade']}")
    else:
        print("No student records available.")

# Function to save the collection to a local file
def save_to_file():
    with open("student_records.json", "w") as file:
        json.dump(students, file)





# Load existing student records from the file if it exists
try: #if file not found
    with open("student_records.json", "r") as file: #correct file closure
        students = json.load(file)
except FileNotFoundError:
    pass

# Main menu
while True:
    print("\nStudent Record Management System")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Print All Records")
    print("4. Sort Records by Grade (Lowest to Highest)")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        add_student()  #print("The user chose to add student")
    elif choice == "2":
        delete_student()
    elif choice == "3":
        print_all_records()
    elif choice == "4":
        sort_records_by_grade()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4/5).")
