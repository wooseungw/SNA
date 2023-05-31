while (True):
    num = int(input("숫자를 입력하세요.:"))
    if num <= 0 :
        print("프로그램을 종료합니다.")
        break
    elif num % 7 == 0:
        print("{}은 7의 배수입니다.".format(num))
    else:
        print("{}은 7의 배수가 아닙니다.".format(num))