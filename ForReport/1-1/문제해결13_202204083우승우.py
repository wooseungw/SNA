def avg(numlist):
    avg = 0 
    sum = 0
    for number in numlist:
        sum += number
    avg = sum/len(numlist)
    return avg

def high_socre(numlist):
    max = numlist[0]
    for number in numlist:
        if max <= number:
            max = number
    
    return max

def low_socre(numlist):
    low = numlist[0]
    for number in numlist:
        if low >= number:
            low = number
    
    return low




socre = [3.1, 3.4, 2.7, 4.1, 4.4]
print("평균 = {}".format(avg(socre)))
print("최댓값 = {}".format(high_socre(socre)))
print("최솟값 = {}".format(low_socre(socre)))
