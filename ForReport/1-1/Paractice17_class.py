#클래스_ 수십 수백게의 오브젝트를 쉽게만드는(붕어빵틀)
# name = "마린"#이름
# hp = 40#체력
# damage = 5#공격력
# print("{}이 생성되었습니다.".format(name))
# print("체력 {0},공격력 {1}".format(hp, damage))

# tank_name = "탱ㅋ"

# def attack(name, location, damage):#함수
#     print("{0}:{1} 방향으로 적국ㄴ을 공격합니다.[공격력{2}]".format(name,location,damage))
    
# attack(name, "1시", damage)

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name #맴버변수 class내 정의되는 변수,초기화,사용 가능
        self.hp = hp
        self.damage = damage
        print("{0}이 생성되었습니다.".format(self.name))
        print("체력{0}, 공격력{1}".format(self.hp, self.damage))
        
marine1 = Unit("마린",40,5)#(self,"마린",40,5) self 생략후 작성, class로 만들어지는 것 객체 
marine2 = Unit("마린",40,5)
tnak1 = Unit("탱크", 150, 35)

wraith1 = Unit("레이스",80,6)
print("멤버변수 가져오기 이름:{0}, hp:{1}, 공격력{2}".format(wraith1.name,wraith1.hp,wraith1.damage))

wraith2 =  Unit("바뀐 레이스",80,6)
wraith2.clocking = True #맴버변수는 밖에서 선언도 가능, 클래스 내부에 영향으로 주지않는다.

if wraith2.clocking == True:
    print("{0}는 클로킹됨".format(wraith2.name))