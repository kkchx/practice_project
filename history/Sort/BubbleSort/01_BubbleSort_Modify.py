## https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/practice-problems/
import random
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # Last i elements are already in place, no need to compare them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Example usage

flag = 0
while flag==0:
    print("choose the algorithm\n 1 - Bubble sort\n 2 - Selection")
    print("Choose the action\n"
          "1 - Use example list\n"
          "2 - Generate Random list\n"
          "3 - Enter list manually\n")
    choice = int(input())

    if choice==1:
        unsorted_list = [5, 2, 9, 1, 5, 6]
    elif choice==2:
        print(f"Input the length of the list")
        length = int(input())
        unsorted_list = [random.randint(0, 10) for _ in range(length)]
    else:
        print(f"Input the length of the list")
        length = int(input())
        unsorted_list = [0]*length
        for i in range (0,length,1):
            print(f"Enter", i, " element")
            unsorted_list[i]=int(input())


    print("Unsorted List:", unsorted_list)
    bubble_sort(unsorted_list)

    print("Sorted List:", unsorted_list)


    print("Would you like to continue? Y/N")
    answer = str(input())
    if answer == 'Y' or answer == 'y':
        flag = 0
    else: flag = 1








##TASKS:
##1. Modify the code of the program to al
##  a) choose user to enter or generate array
##  b) set length of the array