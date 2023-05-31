import sys

numInput = int(sys.stdin.readline())

numstr = bin(numInput)

count =0

for i in range(len(numstr)):
    if (numstr[i] == "1"):
        count +=1
        
print(count)