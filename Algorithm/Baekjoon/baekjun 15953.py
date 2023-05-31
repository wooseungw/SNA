numbers = input("")
numbers = int(numbers)
a_list = []
b_list = []
for i in range(numbers):
    a , b = input("").split( )
    a_list.append(a)
    b_list.append(b)
    
def price1(num1):
    price = 0
    num1 = int(num1)
    if num1 >= 22:
        price = 0
    elif  16 <= num1 <= 21:
        price = 100000
    elif 11 <= num1 <= 15  :
        price = 300000
    elif 7 <= num1 <= 10 :
        price = 500000
    elif 4 <= num1 <= 6:
        price = 2000000
    elif 2 <= num1 <= 3:
        price = 3000000
    elif num1 == 1:
        price = 5000000
    else:
        price = 0
    return price

def price2(num2):
    price = 0
    num2 = int(num2)
    if num2 > 31:
        price = 0
    elif 16 <= num2 <= 31:
        price = 320000
    elif 8 <= num2 <= 15:
        price = 640000
    elif 4 <= num2 <= 7:
        price = 1280000
    elif 2 <= num2 <= 3:
        price = 2560000
    elif num2 == 1:
        price = 5120000
    else:
        price = 0
        
    return price

for i in range(numbers):
    print(price1(a_list[i]) + price2(b_list[i]))