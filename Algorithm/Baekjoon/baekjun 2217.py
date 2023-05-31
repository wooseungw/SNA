import sys
n = int(sys.stdin.readline())
list = []
for i in range(n):
    list.append(int(sys.stdin.readline()))
    
list.sort();    

max =0
for i in range(n):
    temp = list[i]*(n-i)
    
    if( temp > max):
        max = temp
    else:
        continue
    
print(max)