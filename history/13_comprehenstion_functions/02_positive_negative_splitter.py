# Import the constant list
from constants import NUMBER_LIST

# Split numbers into positive and negative using list comprehension
positive_numbers = [num for num in NUMBER_LIST if num > 0]
negative_numbers = [num for num in NUMBER_LIST if num < 0]

# Display the results
print("Original list:", NUMBER_LIST)
print("Positive numbers:", positive_numbers)
print("Negative numbers:", negative_numbers)