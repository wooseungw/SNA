import sys

sum, sub = sys.stdin.readline().split()
sum = int(sum)
sub = int(sub)

if(sum+sub)%2 ==1:
    print("-1")
else:
    a = (sum + sub)//2
    b = sum - a
    if (a<0 or b<0):
        print("-1")
    else:
        if(a>=b):
            print(a,b)
        else:
            print(b,a) 