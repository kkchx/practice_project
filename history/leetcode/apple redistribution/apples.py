def minimumBoxes(apple, capacity):
    sum = 0
    res = 0
    m=0
    for item in apple:
        sum += item
    capacity.sort(reverse=True)

    while sum > 0 and m<len(capacity):
        sum = sum - capacity[m]
        m+=1
        res += 1
    return res