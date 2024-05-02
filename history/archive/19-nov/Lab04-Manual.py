import numpy as np

# Get the size of the square matrix from the user
N = int(input("Enter the size of the square matrix (N > 2): "))

# Ensure N is greater than 2
while N <= 2:
    print("Please enter a value greater than 2.")
    N = int(input("Enter the size of the square matrix (N > 2): "))

# Create a matrix N x N filled with random integers in the range 10 to 25
matrix = np.random.randint(10, 26, size=(N, N))

# Print the created matrix
print("Matrix:")
print(matrix)

# Calculate the sum of diagonals using a for loop
sum_primary_diagonal = sum(matrix[i][i] for i in range(N))
sum_secondary_diagonal = sum(matrix[i][N - i - 1] for i in range(N))

# Print the sum of diagonals
print("Sum of Primary Diagonal:", sum_primary_diagonal)
print("Sum of Secondary Diagonal:", sum_secondary_diagonal)
