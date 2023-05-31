def list_avg(numlist) :
    sum = 0
    avg = 0
    for number in numlist :
        sum += number
    avg = sum/len(numlist)
    return avg
    


math_score = [90, 80, 70, 50, 60]

list_avg(math_score)
