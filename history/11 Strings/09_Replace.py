def replace_spaces(input_string):
    # Using the replace method to replace spaces with "%20"
    replaced_string = input_string.replace(" ", "%20")
    return replaced_string

# Example usage:
user_input = input("Enter a string with spaces: ")
#user_input = "Maldives are the most beautiful islands in the world"
result = replace_spaces(user_input)
print("String with spaces replaced:", result)