


num = 12341

def fun(i):
    if i == num:
        print("함수가 받은 값이 밖의 변수 num과 동일")
        i2 = num + 123341
        return i2
    else:
        print("x")
        
    print("{}ssdddd".format(i2))    
        
fun(12341)

# def recursion(i):
#     if i == 0:
#         return 1
#     else:
#         return i * recursion(i-1)
    
# print(recursion(5))

# memo = {1:1 ,2:1}

# def fibonacci(i):
#     global memo
#     if i in memo:
#         return memo[i]
    
#     if i in memo:
#         return memo[i]
#     else:
#         output = fibonacci(i-1) + fibonacci(i -2)
#         memo[i] = output
#         return output
        
    
    
# print(fibonacci(50))

def test():
    return(123,1244,1232)

a, b, c = test()
print(a)
print(b)
print(c)

