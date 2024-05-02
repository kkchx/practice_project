def count_vowels_consonants(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in input_string if char in vowels)
    consonant_count = len(input_string) - vowel_count
    return vowel_count, consonant_count

# Example usage:
user_input = input("Enter a string: ")
vowels, consonants = count_vowels_consonants(user_input)
print(f"Vowels: {vowels}, Consonants: {consonants}")