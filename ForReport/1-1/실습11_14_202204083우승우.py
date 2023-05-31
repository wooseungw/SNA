def add(num1,num2):
    result = num1 + num2
    return result

def sub(num1,num2):
    if num1 > num2:
        result = num1 - num2
    else:
        result = num2 - num1
    
    return result    
    
def mul(num1,num2):
    result = num1 * num2
    return result

def div(num1,num2):
    result = num1 / num2
    return result

print("─────계산기─────")
num_result =0
while(True):
    num = int(input("1.덧셈 2.뺄셈 3.곱셉 4.나눗셈 5.종료 : "))
    if num == 5:
        break
    else:
        print("정수 2개 입력: ")
        num1 = float(input())
        num2 = float(input())
        
    if num == 1:
        num_result = add(num1, num2)
    elif num ==2:
        num_result = sub(num1, num2)
    elif num ==3:
        num_result = mul(num1, num2)
    else:
        num_result = div(num1, num2)
    print("결과: {}".format(num_result))