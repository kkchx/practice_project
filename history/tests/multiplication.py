# Define the number for which you want to create the multiplication table
number = int(input("Enter a number: "))

# Loop from 1 to 10 and display the multiplication result for each iteration
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
6