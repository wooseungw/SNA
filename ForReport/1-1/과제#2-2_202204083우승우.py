value = int(input("단수?: "))

if 0 < value < 10:
    for i in range(1, 10):
        sum = i * value
        print("{} x {} = {}".format(value, i, sum))
else:
    print("잘못된 단수입니다.")