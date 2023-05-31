shirts_count = int(input("티셔츠 개수: "))
sweater_count = int(input("스웨터 개수: "))

shirts_price = 10000
sweater_price = 30000

price_total = shirts_count * shirts_price + sweater_count * sweater_price
price_total = int(price_total)

if price_total < 100000:
    price_total *= (1 - 0.05)
    
else:
    price_total *= (1 - 0.15)
    
print("총 가격은", int(price_total), "원입니다.")