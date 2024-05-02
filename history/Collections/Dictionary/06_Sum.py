'''
Write a Python program to sum all the items in a dictionary.
'''
d=dict()
for x in range(1,16):
    d[x]=x**2

print(d)
print(sum(d.values()))
