import sys

testCase = int(sys.stdin.readline()) 

for i in range(testCase):
    a,b = sys.stdin.readline().split(" ")
    a = int(a)
    b = int(b) #input a,b
    
    result = 0; #선언
    
    
    b = (b % 4) #제곱의 나머지를 봤을 때 4 주기로 1,2,3,4 의 나머지가 각각 5,6,7,8과 똑같음에서 착안 따라서 b의 값을 1~4사이로 하면 계산량도 줄어서 빠르게 실행가능
    
    if(b==0):
        b = 4
    
    
    
    
    result = (a**b)%10
    if(result == 0):
        result = 10
    
    
    
    print(result)