# check and compare the run time of the algorythms
#https://www.hackerearth.com/practice/algorithms/sorting/selection-sort/tutorial/
import random
import time
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Find the minimum element in the unsorted part of the array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the first element in the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage

flag = 0
while flag==0:
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
        unsorted_list = [random.randint(0, 1000) for _ in range(length)]
    else:
        print(f"Input the length of the list")
        length = int(input())
        unsorted_list = [0]*length
        for i in range (0,length,1):
            print(f"Enter", i, " element")
            unsorted_list[i]=int(input())

    print("Unsorted List:", unsorted_list)
    compare_list = unsorted_list

    start_time = time.time()*1000
    selection_sort(unsorted_list)
    end_time = time.time()*1000
    run_time = end_time-start_time

    print("Sorted List:", unsorted_list)
    print("Run time: ", run_time)


    print("Would you like to continue? Y/N")
    answer = str(input())
    if answer == 'Y' or answer == 'y':
        flag = 0
    else: flag = 1








