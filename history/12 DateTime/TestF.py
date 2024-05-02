def calc_fact(number):
    ...
    result = 0 + number
    ''' the code to calculate factorial'''
    return result


while True:
    user_input = int(input("enter a number to calculate factorial: \n"))
    fact = calc_fact(user_input)
    print(f'{user_input}! is {fact}')
    reply = input("Would you like to continue? y/n")
    if reply != 'y':
        break
