'''
explain task and demonstrate output
analyze the code
perform a step-by-step run to understand how it works
write, execute, modify
'''

def compress_string(input_string):
    compressed_string = ""
    count = 1

    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            compressed_string += input_string[i - 1] + str(count)
            count = 1

    compressed_string += input_string[-1] + str(count) #[-1] last character
    return compressed_string

# Example usage:
user_input = input("Enter a string: ")
result = compress_string(user_input) #function

print("Compressed string:", result)
print("Length of the initial string", len(user_input) )
print("Length of the compressed string", len(result))