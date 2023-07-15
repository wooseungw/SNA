math_score = [45, 66, 70, 83, 50, 77, 87, 92, 73, 89]
 
def max_score(score_list):
    if len(score_list) == 0:
        return False
    
    max = score_list[0]    
    for score in score_list:
        if score > max:
            max = score
    return max

print(max_score(math_score))