num1 = int(input("num1?"))
num2 = int(input("num2?"))
num3 = int(input("num3?"))

if num1 > num2 :
    if num2 > num3 :
        print("가장 작은수는", num3 ,"입니다.")
    else:
        print("가장 작은수는", num2 ,"입니다.")
else:
    if num1 > num3:
        print("가장 작은수는", num3 ,"입니다.")
    else:
        print("가장 작은수는", num1 ,"입니다.")