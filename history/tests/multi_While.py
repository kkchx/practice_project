# Define the number for which you want to create the multiplication table
number = int(input("Enter a number: "))

# Initialize a variable to keep track of the multiplier
i = 1

# Use a while loop to generate the multiplication table
while i <= 10:
    result = number * i
    print(f"{number} x {i} = {result}")
    i += 1
