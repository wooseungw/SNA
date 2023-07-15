num = 1234

def print2(value2,n):
    for i in range(n):
        print(value2)

print2("input",5)

def factorical(n):
    if n ==0:
        return 1
    else:
        return n * factorical(n-1)
print(factorical(0))
print(factorical(4))

d = {1:1,2:1}

def fibo(n):
    if n in d:
        return d[n]
    else:
        output = fibo(n-1) + fibo(n-2)
        d[n] = output
        return output
    
print(fibo(12))

