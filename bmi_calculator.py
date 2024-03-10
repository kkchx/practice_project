#let this function only calculate bmi
def cal_bmi(weight,height):
    result = round(weight/(height/100)**2,1)
    # if result < 18.5
    return result

# create another function to interpret the results
def results_interpretations(bmi):
    if bmi < 18.5:
        return "You are underweight"
    elif bmi <24.9:
        return ""
    ...


# improve the exception handling with try/except blocks
weight = int(input("Enter weight: "))
height = int(input("Enter the height: "))
bmi = cal_bmi(weight,height)
print(f"Your bmi is {bmi} and {results_interpretations(bmi)}")