import sys

n = int(sys.stdin.readline())
times = sys.stdin.readline().split()
times = list(map(int, times))

total = 0

times.sort()

print(n)
print(times)
for i in range(0,n):
    total = times[i]*(n-i)+ total 

print(total)