score = [90,80,70,60,50]
word = ["oneoneoneoneone", "second", "three"]


def averge(list):
    sum = 0
    for i in list:
        sum += i
    
    aver = sum / len(list)
    return aver

def Max(list):
    max = 0
    for i in list:
        if max < i:
            max = i
    
    return max
        
def Pass(list):
    aver = averge(list)
    if aver >= 60:
        print("합격")
    else:
        print("불합격")
        
def find_longert_word(list):
    result = ""
    for i in list:
        
        if len(i) >= len(result):
            result = i
            
    return result
           
def find_shorest_word(list):
    result = list[0]
    for i in list:
            
        if len(i) <= len(result):
            result = i
            
    return result
        
print(averge(score))
print(Max(score))
print(Pass(score))
print(find_longert_word(word))
print(find_shorest_word(word))

contractPrice = int(input("월 납입금:"))
period = int(input("사용 개월수:"))
cardcode = int(input("카드 코드:"))

def period_discount(price, period):
    discount = 0
    if period <= 6:
        price = price
    elif 6 < period <= 12:
        discount = price * 0.1
        price = price * 0.9
    else:
        discount = price * 0.2
        price = price * 0.8
        
    return discount
        
def card_discount(price, code):
    discount = 0
    if code == 11:
        discount = price * 0.05
        price = price * 0.95
    elif code == 12:
        discount = price * 0.08
        price = price * 0.92
    elif code == 13:
        discount = price * 0.12
        price = price * 0.88
        
    return discount

def finalPrice(origin,period,card):
    price = origin - period - card
    return price

print(period_discount(contractPrice,period))
print(card_discount(contractPrice, cardcode))
print(finalPrice(contractPrice,period_discount(contractPrice,period),card_discount(contractPrice, cardcode)))