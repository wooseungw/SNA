import sys

n , k = map(int,sys.stdin.readline().split())
data = []
for i in range(n):
    data.append(int(input()))
data.reverse()

i = 0
count = 0
while(k != 0):
    if(k // data[i] > 0):
        local = 0
        local = k // data[i] 
        count = count + k // data[i] 
        k = k- data[i]*local      
    else:
         i = i + 1
        
print(count)