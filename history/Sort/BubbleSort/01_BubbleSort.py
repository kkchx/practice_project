## https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/practice-problems/

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # Last i elements are already in place, no need to compare them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Example usage
unsorted_list = [5, 2, 9, 1, 5, 6]
print("Unsorted List:", unsorted_list)

bubble_sort(unsorted_list)

print("Sorted List:", unsorted_list)


##TASKS:
##1. Modify the code of the program to allow
##  a) choose user to enter or generate array
##  b) set length of the array