import random
print(f"Please enter the length")
length = int(input())
source_list = [random.randint(1,100) for _ in range(length)]
inverted_list = [0]*length

for i in range(0, length, 1):
    inverted_list[i] = source_list[length-1-i]

print(source_list)
print(inverted_list)