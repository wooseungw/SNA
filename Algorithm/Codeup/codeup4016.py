a,b,c = input("").split( )
a = int(a)
b = int(b)
c = int(c) 

k = []

for i in range(1,100001):
    if a % i ==0 and b % i ==0 and c % i ==0:
        k.append(i)
    

print(max(k))