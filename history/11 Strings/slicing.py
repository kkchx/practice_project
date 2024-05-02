def slicing(input_string, start_index, end_index):
    sliced_portion = input_string[start_index:end_index]
    return sliced_portion

# Example usage:
user_input = input("Enter a string: ")
start_index = int(input("Enter the start index for slicing: "))
end_index = int(input("Enter the end index for slicing: "))

result = slicing(user_input, start_index, end_index)
print("Sliced portion:", result)