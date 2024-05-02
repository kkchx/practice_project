print("Please choose the operator: +, -, *, /")
action = str(input())
print("Please enter FIRST var")
n1 = float(input())
print("Please enter SECOND var")
n2 = float(input())
if action == "+":
    print(n1+n2)
elif action == "-":
    print(n1-n2)
elif action == "*":
    print(n1*n2)
elif action == "/":
    print(n1/n2)
else: print("Invalid operation")

#### now moDIFY THE CODE TO CREATE AN ENDLESS CALCULATOR UNTIL USER WANTS DO CONTINUE