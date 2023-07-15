import random

flower = int(input(": "))
flower_list = []
A = []
i = 0

while i < flower:
    month1 = int(random.randrange(1,13))
    month2 = int(random.randrange(1,13))
    month1 = min(month1, month2)
    month2 = max(month1, month2)
   
    if month1 == 2:
        day1 = int(random.randrange(1,29))
    elif month1 == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        day1 = int(random.randrange(1,32))
    else:
        day1 = int(random.randrange(1,31))
       
    if month2 == 2:
        day2 = int(random.randrange(1,29))
    elif month2 == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        day2 = int(random.randrange(1,32))
    else:
        day2 = int(random.randrange(1,31))   
           
    if month1 == month2:
        if day1 != day2:
            flower_list.append([month1, min(day1, day2), month2, max(day1, day2)])            
            i = i + 1
    else:
        flower_list.append([month1, day1, month2, day2])
        i = i + 1
        
print(flower_list)

                
Num_f = len(flower_list)
MIN = 1300
B = []
C = []
New_list = []

for j in range(Num_f):
    A.append(flower_list[j][0] * 100 + flower_list[j][1])
    B.append(flower_list[j][0] * 100 + flower_list[j][1])

B.sort()
print(B)
print(A)
    
for k in range(Num_f):
    for j in range(Num_f):
        if B[k] == A[j]:
            C.append(j)
            

print(C)   
       
for i in range(Num_f):
    New_list.append(flower_list[C[i]])   
    
print(New_list)