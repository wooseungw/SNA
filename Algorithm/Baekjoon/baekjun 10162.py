input_time = input("")
input_time = int(input_time)
a = 0
b = 0
c = 0
d = -1

while(True):
    if(10*c > input_time):
        c = c - 1
        break
    else:
        c = c + 1  
        continue 

input_time = input_time - 10*c 
a =c // 30
c = c - 30*a
b = c // 6
c = c - 6*b


if(input_time == 0):
    print("{} {} {}".format(a,b,c))
else:
    print("{}".format(d))
    