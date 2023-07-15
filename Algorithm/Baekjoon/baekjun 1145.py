import sys

def gcd(a,b):
    r = a % b
    if r == 0:
        return b
    else:
        gcd(b,r)
        
        


num_input = list(map(int,sys.stdin.readline().split(" ")))


num_input.sort(reverse=1)
print(num_input)





result = num_input[2]*num_input[1]*num_input[0]/gcd(num_input[0],gcd(num_input[2],num_input[1]))

print(result)


