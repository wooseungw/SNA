while True :
    N = int(input("숫자를 입력하세요.: "))
    if N <= 0 :
        break
    for i in range(1,N+1,1):
        print("*" * i)
print("프로그램을 종료합니다.")