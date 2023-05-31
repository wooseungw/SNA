p = int(input("소수p: "))
q = int(input("소수q: "))

N = p*q
#N구하기
print("N은 {}".format(p*q))

p = p - 1
q = q - 1
#최소 공배수 LCM
for i in range (max(p,q), (p*q)+1):
    if i % p == 0 and i % q == 0:
        L = i
        break
print("LCM: {}".format(L))
        
     
E_list = []
#E값 구하기
for i in range(2,50):
    if not(L % i == 0):
        if not(i % 2 ==0 or i%3==0 or i%5 ==0 or i % 7 ==0): 
            E_list.append(i)
        elif (i == 2 or i == 3 or i == 5 or i == 7):
            E_list.append(i)
        

print("E리스트:{}".format(E_list))        
E = int(input("E의 값을 입력: "))

D = []
#D값 구하기
for i in range(500):
    if (i*E) % L ==1:
        D.append(i)

print("D:{}".format(D))
number = int(input("D를 입력하세요.:"))

print("E,N = <{},{}>".format(E,N))
print("D,N = <{},{}>".format(number,N))

code = int(input("평문을 입력하시오.:"))
incode = (code**E) % N
decode = (incode**number) % N

print("암호문 = 평문^E mod N = {}^{} % {} = {}".format(code,E,N,incode))
print("평문 = 암호문^E mod N = {}^{} % {} = {}".format(incode,number,N,decode))