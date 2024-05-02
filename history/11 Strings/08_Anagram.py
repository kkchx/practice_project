def are_anagrams(str1, str2):
    # convert to lowercase
    clean_str1 = ''.join(char.lower() for char in str1 if char!=' ')
    clean_str2 = ''.join(char.lower() for char in str2 if char!=' ')

    #Sort the strings
    clean_str1 = sorted(clean_str1)
    clean_str2 = sorted(clean_str2)
    #print(clean_str2,clean_str1)

    #compare and return
    if clean_str2==clean_str1:
        return True
    else: return False


# Example usage:
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if are_anagrams(string1, string2):
    print("The entered strings are anagrams.")
else:
    print("The entered strings are not anagrams.")