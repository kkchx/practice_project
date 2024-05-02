"""
Generate a list containing the length of each word in the input sentence.

Parameters:
- sentence: Input sentence as a string.

Returns:
- List containing the length of each word.
"""
def word_length_counter(sentence):

    words = sentence.split()
    return [len(word) for word in words]

# Example usage
input_sentence = "This is a sample sentence for word length counting."
word_lengths = word_length_counter(input_sentence)

# Display the results
print("Input sentence:", input_sentence)
print("Word lengths:", word_lengths)
