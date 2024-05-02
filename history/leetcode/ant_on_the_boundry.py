
def ant_on_the_boundry(num):
    count = 0
    position=0
    for item in num:
        position += item
        if position == 0:
            count += 1
    return count


list_num = [2,-2,5,-3,-2,1]

nums = []




print(ant_on_the_boundry(list_num))
