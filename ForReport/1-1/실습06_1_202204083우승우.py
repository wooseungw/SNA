num1 = int(input("num1 입력:"))
num2 = int(input("num2 입력:"))

if num1 > 0:
    if num2 > 0:
        print("두 수의 곱은 양수입니다.")
    else:
        print("두 수의 곱은 음수입니다.")
else:
    if num2 > 0:
        print("두 수의 곱은 음수입니다.")
    else:
        print("두 수의 곱은 양수입니다.")
