from array import array
import sys

n = int(sys.stdin.readline())
change = 1000 - n
fiv_hun = change // 500
change = change - fiv_hun*500
one_hun = change // 100
change = change - one_hun*100
fiv_ten = change // 50
change = change - fiv_ten*50
one_ten = change // 10
change = change - one_ten*10
fiv = change // 5
change = change - fiv * 5
one = change
print("{}".format(fiv_hun+one_hun+fiv_ten+one_ten+fiv+one))
