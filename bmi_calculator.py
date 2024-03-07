def cal_bmi(weight,height):
    result = round(weight/(height/100)**2,1)
    if result < 18.5
    return result

weight = int(input("Enter weight: "))
height = int(input("Enter the height: "))
print("Your bmi is",cal_bmi(weight,height))