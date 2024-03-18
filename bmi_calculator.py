try:
    def cal_bmi(weight,height):
        result = round(weight/(height/100)**2,1)
        return result

    def ana_li_ze():
        result = cal_bmi(weight,height) # this is extra
        if result < 18.5:
            print("you're underweight")
        elif result < 24.9:
            print("you're healthy")
        elif result < 29.9:
            print("you're overweight")
        else:
            print("you're obese")


    weight = int(input("Enter weight: "))
    height = int(input("Enter the height: "))
    # create a global BMI var
    bmi = cal_bmi(weight,height)
    print("Your bmi is",bmi,ana_li_ze())
except ValueError:
    print("Please enter number")