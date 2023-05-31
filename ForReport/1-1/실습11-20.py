def coffee(coffee):
    result = 0
    if coffee == "아메리카노":
        result = 4000
    elif coffee == "카페라떼":
        result = 5000
    elif coffee == "카페모카":
        result = 5000    
    elif coffee == "그린티라떼":
        result = 5000    
    
    return result

def size(size):
    result = 0
    if size == 1:
        result = 0
    elif size == 2:
        result = 500
    elif size == 3:
        result = 1000
    return result

def price(coffee_price,size_price):
    result = coffee(coffee_price) + size(size_price)
    return result

coffee2 = input("메뉴 이름을 입력하세요.: ")
size2 = int(input("사이즈 번호를 입력하세요. 1:레귤러 2:라지 3:그란데:"))
print("가격은 {}원 입니다".format(price(coffee2,size2)))