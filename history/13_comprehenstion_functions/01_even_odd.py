# Even-Odd Classifier:

# Create a program that takes a list of numbers and
# categorizes them into even and odd using
#   a) loops
#   b) list comprehension.
#
#   Syntax for List Comprehension:
#   new_list = [expression for item in iterable if condition]

# Import the constant list
from constants import NUMBER_LIST


# Initialize empty lists for even and odd numbers
even_numbers = []
odd_numbers = []

# Categorize numbers into even and odd using traditional loops
for num in NUMBER_LIST:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("Original list:", NUMBER_LIST)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

# Categorize numbers into even and odd using list comprehension
even_numbers = [num for num in NUMBER_LIST if num % 2 == 0]
odd_numbers = [num for num in NUMBER_LIST if num % 2 != 0]

# Display the results
print("Original list:", NUMBER_LIST)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)


# Categorize numbers into even and odd using list comprehension
even_numbers = [num for num in NUMBER_LIST if num % 2 == 0]
odd_numbers = [num for num in NUMBER_LIST if num % 2 != 0]

# Display the results
print("Original list:", NUMBER_LIST)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)