import random
length = int(input("Enter length: "))
find = int(input("Enter a number: "))
sourcelist = [random.randint(0,10) for _ in range(length)]
print(sourcelist)
min = sourcelist[0]
max = sourcelist[0]
position = 0
flag = 0
count = 0
for i in range(1,length-1,1):
    if sourcelist[i] > max:
        max = sourcelist[i]
    if sourcelist[i] < min:
        min = sourcelist[i]
    if find == sourcelist[i]:
        flag = 1
        count+=1
        position = i+1
print("minimum is ",min)
print("maximum is ",max)
if flag == 1:
    print("Present,", count, "times, last position is", position,)