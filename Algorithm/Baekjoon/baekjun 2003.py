import sys

n,m = sys.stdin.readline().split(" ")

n = int(n)
m = int(m)

list_0 = []
list_0 = sys.stdin.readline().split(" ")

list_0 = list(map(int,list_0))

lence = len(list_0)
count = 0

for i in range(lence):
    buff = list_0[i]

    for j in range(i+1,lence):
        if j == i:
            continue
        else:
            if buff + list_0[j] > m:
                continue
            elif buff + list_0[j] < m:
                buff += list_0[j]
            else:
                count += 1
            
print(count)    
    