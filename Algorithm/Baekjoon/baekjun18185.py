import random

fac = int(input(""))

# if 3<= fac <= 10000:
#    print(fac)
# else:
#     print("값을 다시 입력하세요")

list_i = []

for i in range(fac):
    list_i.append(random.randrange(0,10^4 +1))
    
list_i.append(0)
list_i.append(0)
    
print(list_i)
print(len(list_i)) 

# a = len(list_i) // 3 #리스트의 길이 구해서 3등분
# b = len(list_i) % 3 #리스트 나머지
# print(a)
# print(b)
st7 = 0
st5 = 0
st3 = 0
i = 0
while i != len(list_i)-2:
    if list_i[i] != 0:
        if list_i[i+1] != 0:
            if list_i[i+2] != 0:
                list_i[i] = list_i[i] - 1
                list_i[i+1] = list_i[i+1] - 1
                list_i[i+2] = list_i[i+2] - 1
                st7 = st7 +1
            else:
                list_i[i] = list_i[i] - 1
                list_i[i+1] = list_i[i+1] - 1
                st5 = st5 + 1
        else:
            list_i[i] = list_i[i] - 1
    else:
        i = i + 1
ans = 7*st7 + 5*st5 + 3*st3
print(ans)