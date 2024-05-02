def calc_sum(num):
    word_int = str(num)
    int_list = []
    res=0
    '''
        for i in range(len(word_int)):
           int_list.append(int(word_int[i]))
        
        this looks heavy, 
        there's another more readable option  
        
        for i in range(len(int_list)):
            res += int_list[i]

    '''
    for char in word_int:
        int_list.append(int(char))

    for item in int_list:
        res += item


    return res

numbers = 987654321987654321
sum = calc_sum(numbers)
print(f"The sum of elements is {sum}")