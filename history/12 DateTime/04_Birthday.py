'''
Birthday Reminder:
Create a program that takes a user's birthdate as input and then calculates and
displays the user's age. Use strftime() to format the current date and time, and
calculate the difference to determine the age.
Additionally, you can display a birthday message if it's the user's birthday.
'''

from datetime import datetime

def calculate_age(birthdate):
    today = datetime.now()
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def main():
    print("Welcome to the Birthday Reminder!")

    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")

    age = calculate_age(birthdate_str)
    print(f"You are {age} years old.")

    today = datetime.now()
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").replace(year=today.year)

    if today.date() == birthdate.date():
        print("Happy Birthday!")

main()
