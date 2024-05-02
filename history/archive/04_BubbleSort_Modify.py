#modify the code of basic bubblesory to enable the user set the length of the array
#after sorting count how many duplicates are found
#create a function for it

import random
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place, no need to compare them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def find_duplicates(arr):
    dup_list=[0]
    counter=0
    for i in range(len(arr)-1):
        if arr[i]==arr[i+1] and arr[i]!=dup_list[counter]:
            dup_list.append(arr[i])
            counter+=1
    return counter

# Example usage
print(f"Please input the length of the array")
length = int(input())
unsorted_list=[random.randint(0,50) for _ in range(length)]
print("Unsorted List:", unsorted_list)

bubble_sort(unsorted_list)
count = find_duplicates(unsorted_list)
print("Sorted List:", unsorted_list)
print("Exclusive Duplicates:", count)