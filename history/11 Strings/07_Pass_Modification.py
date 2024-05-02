import random
import string
import pyperclip  # pip install pyperclip


def generate_password():
    length = int(input("Enter the desired password length: "))

    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_punctuation = input("Include punctuation? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'

    characters = ''
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase

    if not characters:
        print("Error: You must select at least one type of character.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))

    # Copy the password to clipboard
    pyperclip.copy(password)

    return password


# Example usage:
generated_password = generate_password()

if generated_password:
    print("Generated Password:", generated_password)
    print("Password has been copied to clipboard.")