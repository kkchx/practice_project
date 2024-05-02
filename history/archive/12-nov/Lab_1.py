import random

def separate_even_odd(input_list):
    even_list=[]
    odd_list=[]
    for i in range(0, length, 1):
        if (input_list[i] % 2) == 0:
            even_list.append(input_list[i])
        else: odd_list.append(input_list[i])
    return even_list, odd_list


length = int(input("Enter the length of the list: "))
source_list = [random.randint(1, 100) for _ in range(length)]
even_list, odd_list = separate_even_odd(source_list)

print(f"Source List: {source_list}")
print(f"Even List: ", even_list,", Sum: ", sum(even_list))
print(f"Odd List: ", odd_list, " Sum: ", sum(odd_list))