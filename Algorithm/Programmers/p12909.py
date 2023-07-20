def solution(s):
    count = 0
    
    for i in s:
        if count < 1 and i == ')':
            return False
        if i =='(':
            count += 1
        else:
            count -= 1
    
    return True if count == 0 else False       
    
        
print(solution('()())(()'))