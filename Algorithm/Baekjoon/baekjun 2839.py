n = int(input(""))

a = n // 5
b = 0

while (True):
    if((n-a*5) % 3 == 0):
        if(a<0):
            print("{}".format(a))
            break
        b = (n-a*5) // 3
        print(a+b)
        break
    else:
        a = a -1
        continue
    
    if(a == 0 and b == 0):
        print("-1")
        break
    



