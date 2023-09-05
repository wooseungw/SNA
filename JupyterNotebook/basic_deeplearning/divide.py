import sys

numInput = int(sys.stdin.readline())
div_list = []

for i in range(1, numInput+1):
    if numInput % i == 0:
        div_list.append(i)

print(div_list)
print(sum(div_list))