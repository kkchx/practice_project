## check the code, find the mistakes to produce the correct output
import random
print(f"Input the length of the list")
length = int(input())
if (length%2)!=0:
    print("length is ODD. Will be shortened by 1")
    length=length-1
source_list=[random.randint(0,10) for _ in range(length)]
length2 = int(length/2)
result_list= [0] * length2

for i in range(0,length2,1):
    result_list[i]=source_list[i*2]+source_list[i*2+1]

print(source_list)
print(result_list)