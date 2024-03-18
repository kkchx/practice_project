def cal_bmi(weight,height):
    try:
        result = round(weight/(height/100)**2,1)
    except ZeroDivisionError:
        print("Height can't be zero")
        return -1
    else:
        return result

def ana_li_ze(bmi):
    if bmi < 18.5:
        return "you're underweight"
    elif bmi < 24.9:
        return "you're healthy"
    elif bmi < 29.9:
        return "you're overweight"
    else:
        return "you're obese"

try:
    weight = int(input("Enter weight: "))
    height = int(input("Enter the height: "))
except ValueError:
    print("Please enter number")
else:
    # create a global BMI var
    bmi = cal_bmi(weight,height)
    if bmi !=-1:
        print(f"Your bmi is {bmi}, {ana_li_ze(bmi)}")