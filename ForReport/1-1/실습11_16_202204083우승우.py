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

score = [95, 90, 45, 10, 80, 100]
print("학생들의 점수는 {} 입니다.".format(score))
num = int(input("1.평균 2.최고점 3.최저점 : "))
if num ==1:
    print("평균 점수: {}".format(avg(score)))
elif num == 2:
    print("최고 점수: {}".format(high_socre(score)))
else:
    print("최저 점수: {}".format(low_socre(score)))

    
    