a_temp, b_temp = input("").split( )
a_temp = int(a_temp)
b_temp = int(b_temp)

st10 = 0
st1 = 0
st5 = 0
while b_temp != a_temp:
    if abs(b_temp - a_temp) <= 2:
        st1 = abs(b_temp - a_temp)
        break
    elif abs(b_temp - a_temp) <= 7:
        st5 = 1
        st1 = abs(abs(b_temp - a_temp) - 5)
        break
    else:
        if a_temp <= b_temp:
            a_temp = a_temp + 10
        else:
            b_temp = b_temp + 10
        st10 = st10 + 1
        
print(st10 + st5 + st1)