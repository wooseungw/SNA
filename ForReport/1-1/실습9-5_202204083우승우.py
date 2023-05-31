n = int(input("숫자를 입력하시오: "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i
    
print("{}! = {}".format(n,fact))