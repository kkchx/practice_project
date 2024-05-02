def reverse_string(input_string):
    reversed_string = input_string[::-1]
    return reversed_string

# Example usage:
user_input = input("Enter a string: ")
result = reverse_string(user_input)
print("Reversed string:", result)