flag = 0
while flag == 0:
    print("Please choose the operator: +, -, *, /")
    action = str(input())
    print("Please enter FIRST var")
    n1 = float(input())
    print("Please enter SECOND var")
    n2 = float(input())
    if action == "+":
        print(n1 + n2)
    elif action == "-":
        print(n1 - n2)
    elif action == "*":
        print(n1 * n2)
    elif action == "/":
        print(n1 / n2)
    else:
        print("Invalid operation")

    print("Would you like to continue? Y/N")
    answer = str(input())
    if answer == 'Y' or answer =='y':
        flag = 0
    else: flag =1
