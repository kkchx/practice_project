import random
def bubble_sort(arr):
    print("Sourse array", arr)
    n = len(arr)

    for i in range(n):
        # Last i elements are already in place, no need to compare them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print("Sorted array: ", arr)
    return arr

def selection_sort(arr):
    print("Sourse array", arr)
    n = len(arr)

    for i in range(n):
        # Find the minimum element in the unsorted part of the array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the first element in the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print("Sorted array: ", arr)

def generate_array(arr):
    print(f"Input the length of the list")
    length = int(input())
    arr=[]*length
    arr = [random.randint(0, 100) for _ in range(length)]

# Example usage


sample_list = [5, 2, 9, 1, 5, 6]


# Main menu
while True:
    print("\nSorting Algorithms")
    print("1. Generate an array")
    print("2. Do the BUBBLE sort")
    print("3. Do the SELECTION sort")
    print("4. Sort Records by Grade (Lowest to Highest)")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        array=[]
        generate_array(array)
    elif choice == "2":
        array=sample_list
        array = bubble_sort(array)
    elif choice == "3":
        array=sample_list
        selection_sort(array)
    elif choice == "4":
        print("Not Ready Yet")#sort_records_by_grade()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4/5).")