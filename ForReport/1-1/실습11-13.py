input_floor = int(input("가고 싶은 층을 입력하세요.:"))
now_floor = int(input("지금 있는 층을 입력하세요.:"))

def inspect(input,now):
    if input > 6 or now > 6:
            print("없는 층계입니다. 다시 입력하세요.")
            return True
            
    if input == now:
        print("다른 층을 눌러주세요.")
        return True
    
    return False
    
        
def ev(input,now):
    if inspect(input_floor, now_floor) == False:
        print("검사 완.")
        if input < now:
            for i in range(now - input + 1):
                print("현재층은{}입니다.".format(now))
                if input == now:
                    print("{}층에 도착했습니다.".format(now))
                now = now - 1
        elif now < input:
            for i in range(input - now + 1):
                print("현재층은{}입니다.".format(now))
                if input == now:
                    print("{}층에 도착했습니다.".format(now))
                now = now + 1
        
        
print(ev(input_floor,now_floor))