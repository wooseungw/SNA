from ctypes import WinDLL
from ssl import DefaultVerifyPaths
from termios import VDISCARD
from this import d
from tkinter import W


apple_price = 500
grape_price = 800
plum_price = 300
print("""사과 = {0} 원
포도 = {1} 원
자두 = {2} 원
      """.format(apple_price,grape_price,plum_price))

cnt_apple = input("사과?")
cnt_apple = int(cnt_apple)
cut_grape = input("포도?")
cut_grape = int(cut_grape)
cnt_plum = input("자두?")
cnt_plum = int(cnt_plum)

total = apple_price * cnt_apple + grape_price * cut_grape + plum_price * cnt_plum
print("전체 구매 가격은",total,"원 입니다.")


