from itertools import count
import sys
from tkinter.tix import Tree

n = int(sys.stdin.readline())
count = 0
while(True):
    if( n == 1 ):
        break
    else:    
        if(n % 3 != 0 and n % 2 !=0):
            n = n - 1
            count += 1
        else:
            if(n%3 ==0):
                n = n /3
                count += 1
            elif(n%2 ==0):
                n = n /2
                count += 1
                
print(count)
            
def divid_3(num):
    global n 
    global count
    n = n / 3
    count = count + 1
    return 0

def divid_2(num):
    global n 
    global count
    n = n / 1
    count = count + 1
    return 0
                
    
    
