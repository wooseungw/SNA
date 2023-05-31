fruit_price = {"배":2000,"사과":1500,"딸기":1800,"참외":2300}
fruit_count = {"배":3,"사과":5,"딸기":2,"참외":5}
sum = 0
for i in fruit_price:
    price = fruit_price[i]*fruit_count[i]
    sum += price
    
print("과일 가격의 총합은 {} 원입니다.".format(sum))
    
    