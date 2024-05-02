'''
using Numpy declare an array of 0 (length 10)
using loop fill it with random numbers from 1.00 to 1.99
using numpy SORT the array, find min and sum
'''
import random
import numpy as np
array = np.zeros(10)

for i in range (10):
    array[i] = round(random.uniform(1.00, 1.99),2)
print(array)
print(f"Sum of array is {round(array.sum(),0)}")
print(f"Min of array is {array.min()}")
print(f"Max of array is {array.max()}")
array = np.sort(array)
print(f"Sorted array is {array}")

'''
using Numpy declare an array of N>2, entered by user
using loop fill it with random numbers from 10 to 50
using numpy SORT the array, find min and sum
'''