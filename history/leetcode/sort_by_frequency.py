def frequencySort(s):
    # Step 1: Count the frequency of each character
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1

    # Step 2: Sort the characters based on their frequencies
    sorted_chars = sorted(frequency, key=lambda x: frequency[x], reverse=True)

    # Step 3: Generate the sorted string
    sorted_string = ''.join(char * frequency[char] for char in sorted_chars)

    return sorted_string


# Test cases
print(frequencySort("tree"))  # Output: "eert" or "eetr"
print(frequencySort("cccaaa"))  # Output: "aaaccc" or "cccaaa"
