pencil_price = 1000
pen_price = 2000

print("연필 = {0}원".format(pencil_price))
print("펜 = {0}원".format(pen_price))

num_pencil = input("연필은 몇 개를 구입하시겠습니까?")
num_pencil = int(num_pencil)

num_pen = input("펜은 몇 개를 구입하시겠습니까?")
num_pen = int(num_pen)

total_price = pencil_price * num_pencil + pen_price * num_pen
print("총 가격은 {0}원 입니다.".format(total_price))