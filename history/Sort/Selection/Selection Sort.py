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

unsorted_list = [5, 2, 9, 1, 5, 6]
print("Unsorted List:", unsorted_list)

selection_sort(unsorted_list)

print("Sorted List:", unsorted_list)

##TASKS:
##1. Modify the code of the program to allow
##  a) choose user to enter or generate array
##  b) set length of the array
c