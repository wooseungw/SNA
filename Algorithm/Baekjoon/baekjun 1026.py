import sys

result = 0
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

a.sort()
b.sort()
b.reverse()

for i in range(n):
    result += a[i]*b[i]
    
print("{}".format(result))


