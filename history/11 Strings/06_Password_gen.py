'''
explain the task and demonstrate the output
analyze code
run and perform

HW: expand to allow user
1) enter the length
2) ask if he wants to use digits, punctuation, upper and lowe-case letters
3) copy the generated password to clipboard
'''

import random
import string
import pyperclip

def generate_password(length=12):
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage:
password = generate_password()
pyperclip.copy(password)
print(password, "Copied to Clipboard!")