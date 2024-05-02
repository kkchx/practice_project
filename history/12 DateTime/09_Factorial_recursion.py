from datetime import datetime
def calculate_factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * calculate_factorial(n-1)


while True:
    n = int(input("Please enter the number to calculate factorial: \n"))
    start_time = datetime.now()
    factorial = calculate_factorial(n)
    ent_time = datetime.now()
    duration = ent_time - start_time
    print(f"{n}! = {factorial}")
    print(f"Duration is {duration.seconds} seconds or {duration.microseconds} microseconds" )
    if input("Would you like to repeat? (y/n)")=='n':
        break