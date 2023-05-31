import sys

a,b,c = map(float,sys.stdin.readline().split())

if b>c:
    r = a * b /c    
else:
    r =  a / b *c

r = int(r)
print(r)