'''
declare a 2 d array using numpy
'''
import numpy as np
import random
matrix = np.zeros((3,3))

for i in range(3):
    for j in range(3):
        matrix[i][j]=round(random.randint(1,10))

print(matrix)
