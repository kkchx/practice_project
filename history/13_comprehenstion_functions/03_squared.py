# Create a function that generates a new list containing
# the square of each number from a given list using list comprehension.

def square_numbers(input_list):
    res = [num ** 2 for num in input_list]
    return res

# Import the constant list
from constants import NUMBER_LIST

# Use the function to square the numbers
squared_numbers = square_numbers(NUMBER_LIST)

# Display the results
print("Original list:", NUMBER_LIST)
print("Squared numbers:", squared_numbers)