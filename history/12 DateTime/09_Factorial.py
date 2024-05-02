from datetime import datetime
def calculate_factorial(n):
    result = 1
    for i in range(1, n+1,1):
        result *= i
    return result
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