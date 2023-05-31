

class unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        
        print("{}이 생성되었습니다. hp:{}".format(self.name,self.hp))
        
    def move(self, location):
        print("[지상유닛 이동]")
        print("{}: {}방향으로 이동합니다. [속도:{}]".format(self.name,location,self.speed))
        
        
        
class AttackUnit(unit):
    def __init__(self, name, hp, speed, damage):
        unit.__init__(self ,name, hp, speed)
        self.damage = damage
        
    def attack(self, location):
        print("{}이 {}쪽으로 공격합니다. 공격력: {}".format(self.name, location, self.damage))
        
    def damaged(self, damage):
        print("{}이 {}만큼 피해를 입었습니다.".format(self.name,damage))
        self.hp -= damage
        print("{}의 체력이 {}남았습니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{}이 파괴되었습니다.".format(self.name))
        
        
class FlyUnit:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed
        
    def fly(self, name, location):
        print("{}:{}방향으로 날아갑니다. 속도:{}".format(name, location, self.flying_speed))
        
class FlyAtacckUnit(AttackUnit,FlyUnit):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        FlyUnit.__init__(self, flying_speed)
        
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name,location)    
    
class BuildingUnit(unit):
    def __init__(self, name, hp, location):
        #pass   #변수 칸이 비어도 일단 넘어감
        #unit.__init__(self, name, hp ,0) == super().__init__(name, hp, 0)
        super().__init__(name, hp, 0)#다중 상속시 문제발생 다중상속시 맨앞의 부모클래스만 불러온다.

        
medic1 = unit("메딕",50,1)
marine1 = AttackUnit("마린",50,1,5)
tank1 = AttackUnit("탱크",150,2,25)
vlakyrie = FlyAtacckUnit("발키리",170,7,7)


vlakyrie.attack("3시")
marine1.attack("1시")
tank1.damaged(marine1.damage)


tank1.seige = True

if tank1.seige == True:
    tank1.damage = 75
    print("{}는 시즈모드입니다. 공격력{}".format(tank1.name,tank1.damage))
    
marine1.damaged(tank1.damage)

marine1.move("1시")
vlakyrie.move("11시")
