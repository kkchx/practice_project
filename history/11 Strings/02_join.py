'''
def concatenate_with_join(string_list):
    concatenated_string = ''.join(string_list)
    return concatenated_string

# 1st Example: iterables
string_list = ["Hello", " ", "World", "!"]
result = concatenate_with_join(string_list)
print("Concatenated string:", result)
'''

'''
#2nd Example separator

numlist = ['1', '3', '5', '7', '9']
separator = '<->'

print('List before Join():', numlist)
print('List after Join():' , separator.join(numlist))

'''

#3rd Example - strings


# .join with string
str1 = 'YXZ'
str2 = '1234'

print(str1.join(str2))
print(str2.join(str1))

string = 'Hello'
print('.'.join(string))
