import random
import math
z = int(input("Enter length: "))
mylist = []
mylist2 = []
mylist1 = ",".join(str(random.randint(1,10)) for _ in range(0,z))
print("[",mylist1,"]")
f = math.floor(z/2)
for i in range(0,f):
    listlen = len(mylist1)
    print(f)