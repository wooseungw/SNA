time = input("")
time = int(time)
money = []
a = 0
b = 0
c = 0
penny = 0
for i in range(time):
    money_input = input("")
    money_input = int(money_input)
    money.append(money_input)
    
for i in money:
    while(True):
        if(1*penny > i):
            penny = penny - 1
            break
        else:
            penny = penny + 1  
            continue 

    a = penny // 25
    penny = penny - 25*a
    b = penny // 10
    penny = penny - 10*b
    c = penny // 5
    penny = penny - 5*c

    print("{} {} {} {}".format(a,b,c,penny))