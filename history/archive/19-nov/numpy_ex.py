import numpy_ex as np

a_zeros = np.zeros(5)
a_ones = np.ones(5)
a_random = np.empty(5)

print(a_zeros)
print(a_ones)
print(a_random)

for i in range(5):
    a_zeros[i] = a_zeros[i]*i
    a_ones[i] = a_ones[i]*i
    a_random[i] = a_ones[i]*i

print(a_ones,'\n', a_zeros,'\n', a_random,'\n')