def is_palindrome(input_string):
    #cleaned_string = ''.join(char.lower() for char in input_string)
    cleaned_string = str.lower(input_string)
    return cleaned_string == cleaned_string[::-1]

# Example usage:
user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print("The entered string is a palindrome.")
else:
    print("The entered string is not a palindrome.")