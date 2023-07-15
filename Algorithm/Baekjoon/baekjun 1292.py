import sys 

a,b = sys.stdin.readline().split(" ")
a = int(a)
b = int(b)

gap = b-a + 1
a -= 1


numplus = 0
indexnum = 0 

i=0
while(a !=0):
    numplus += 1
    for i in range(numplus):
        if (a==0):
            indexnum = i
            
            break
        a -= 1
        

sum =0
while(gap):
    if (indexnum ==0):
        numplus += 1 
        
    for i in range(indexnum,numplus):
        if (gap ==0):
            break
        gap -= 1
        sum += numplus
    
    indexnum =0
    
    

print(sum)
        
        