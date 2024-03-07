def cal_bmi(weight,height):
    return round(weight/(height/100)**2,1)


weight = int(input("Enter weight: "))
height = int(input("Enter the height: "))
print("Your bmi is",cal_bmi(weight,height))