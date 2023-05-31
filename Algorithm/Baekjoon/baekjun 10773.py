import sys

case = int(sys.stdin.readline())
stack = []
count = 0
for i in range(case):
    buff = int(sys.stdin.readline())
    
    if buff == 0:
        del stack[count-1]
        count -= 1
    else:
        stack.append(buff)
        count += 1

sum = 0
for i in stack:
    sum += i
    
print(sum)