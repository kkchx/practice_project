import random
def compare(a,b):
    if a == b:
        return 0
    elif a < b:
        return 1 # user guess too high
    else:
        return -1


num = random.randint(0,100)
user_input = int(input("Enter a number: "))
tries_number = 0
while True:
    guess_result = compare(num,user_input)
    if guess_result == 0:
        print("You win")
        print(tries_number,"tries")
        break
    elif guess_result == -1:
        print("Too low")
        tries_number+=1
        user_input = int(input("Enter a number: "))
    else:
        print("Too high")
        tries_number+=1
        user_input = int(input("Enter a number: "))