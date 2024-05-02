#user enters a word and a letter
#program counts how many times the letter appears in the word

print(f"Enter a word")
word = input()


print(f"Enter a test letter")
char = input()
length = len(word)

word_list = ['']*length
counter = 0

for i in range (0, length-1, 1):
    if word[i]==char:
        counter+=1

print(counter)
