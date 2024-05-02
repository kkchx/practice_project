# Function to print a matrix
def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")  # Print each element with a space as separator
        print()  # Move to the next row after printing all elements in the current row

# Function to perform bubble sort on a 2D matrix
def bubble_sort_2d(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(0, cols - i - 1):
            # Compare adjacent elements
            if matrix[0][j] > matrix[0][j + 1]:
                # Swap the rows if necessary
                matrix[0][j], matrix[0][j + 1] = matrix[0][j + 1], matrix[0][j]

# Example 2D matrix
matrix = [
    [5, 2, 9],
    [8, 1, 4],
    [6, 3, 7]
]

print("Original Matrix:")
print_matrix(matrix)

bubble_sort_2d(matrix)

print("\nSorted Matrix:")
print_matrix(matrix)
