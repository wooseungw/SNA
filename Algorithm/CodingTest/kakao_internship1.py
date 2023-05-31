def solution(survey, choices): 
    
    global dic
    dic = {'RT': 0,'CF':0,'JM':0,'AN':0}
    
    temp  = len(survey)
    for i in range(0,temp):
        
        buff = survey[i]
        num = choices[i]
        if(buff == "RT"):
            cal(buff,num)
        
        elif buff == "CF":
            cal(buff,num)
        
        elif buff == "JM":
            cal(buff,num)
        
        elif buff == "AN":
            cal(buff,num)
        
        elif buff == "TR":
            cal_rev(buff,num)
        
        elif buff == "FC":
            cal_rev(buff,num)
        
        elif buff == "MJ":
            cal_rev(buff,num)
        
        elif buff == "NA":
            cal_rev(buff,num)
        
        
    for i ,k in dic.items():
        
        if(k<0):
            answer += i[1]
        else:
            answer += i[0]
    
    
    
    return answer

def cal(buff,num):
    if buff == "RT":
        
            dic['RT'] += num-4
        
    elif (buff == "CF"):
        
            dic['CF'] += num-4
        
    elif (buff == "JM"):
        
            dic['JM'] += num-4
        
    elif(buff == "AN"):
        
            dic['AN'] += num-4
        
    
def cal_rev(buff,num):
    if(buff == "TR"):
        dic['RT'] += -(num-4)
        
    elif(buff == "FC"):
        dic['CF'] += -(num-4)
        
    elif(buff == "MJ"):
        dic['JM'] += -(num-4)
        
    elif(buff == "NA"):
        dic['AN'] += -(num-4)
        