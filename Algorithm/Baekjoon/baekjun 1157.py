import sys

instring = sys.stdin.readline().strip()
instring = instring.upper()

strlen = len(instring)
biggest =0
bigger = 0
biggerchar = '\0'
biggestchar = '\0'

#문자열 입력 받은 후 입력받은 문자열에서 아스키코드65번의 개수찾기~90까지
for i in range(65,91):
    i = chr(i)
    buff = instring.count(i)
    if buff > biggest:
        biggestchar = i
        biggest = buff
    if buff == biggest and i != biggestchar:
        bigger = biggest


if bigger == biggest:
    print("?")
else:
    print(biggestchar)