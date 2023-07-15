#일반가격 함수
def price(people):
    print("{}명 가격은 {}원 입니다.".format(people, people * 10000))
    
#조조할인
def price_moring(people):
    print("{}명 조조할인 가격은 {}원 입니다.".format(people, people * 6000))
    
#군인할인
def price_soldier(people):
    print("{}명 군할인 가격은 {}원 입니다.".format(people, people * 4000))