'''
create a matrix N*N, where N is >2
fill randomly in range 10..25
calculate a sum of diagonals
'''

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

# Calculate the sum of diagonals
sum_diagonals = np.trace(matrix) + np.trace(np.fliplr(matrix))

# Print the sum of diagonals
print("Sum of Diagonals:", sum_diagonals)