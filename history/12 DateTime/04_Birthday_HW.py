'''
Birthday Reminder:
Create a program that takes a user's birthdate as input and then calculates and
displays the user's age. Use strftime() to format the current date and time, and
calculate the difference to determine the age.
Additionally, you can display a birthday message if it's the user's birthday.
'''

from datetime import datetime, timedelta


def calculate_age(birthdate):
    today = datetime.now()
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    age_years = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    age_months = 12 - abs(today.month - birthdate.month - (today.day < birthdate.day))
    age_days = 31 - abs(today.day-birthdate.day)
    age = f"{age_years} years, {age_months} months, {age_days} days"
    return age

def calculate_age2(birthdate):
    today = datetime.now()
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")

    # Set the target date for the next New Year
    if today.month > birthdate.month:
        birthdate_target = datetime(today.year + 1, birthdate.month, birthdate.day, 0, 0, 0)
    else:
        birthdate_target = datetime(today.year,birthdate.month, birthdate.day)

    # Calculate the time remaining
    time_remaining = birthdate_target - today
    if time_remaining.days>31:
        months_remaining = time_remaining.days//31
        days_remaining = time_remaining.days - months_remaining * 31
        left = f"Time remaining: {months_remaining} months, {days_remaining} days"
    else:
        left = f"Time remaining:{time_remaining.days} days"
    return left
def main():
    print("Welcome to the Birthday Reminder!")

    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")

    age = calculate_age(birthdate_str)
    left = calculate_age2(birthdate_str)
    print(age)
    print(left)

    today = datetime.now()
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").replace(year=today.year)

    if today.date() == birthdate.date():
        print("Happy Birthday!")

main()
