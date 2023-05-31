
'''
number = int(input("숫자입력:"))

if number % 2 == 0:
    print("숫자는 짝수입니다.")
else:
    print("입력 숫자는 홀수입니다.")
   '''
#list = [2, 3, [1,2,3,4,2]]
#print(list[-1])s
#print(list[2])

list = [2,5,6,6,72,2,2,1,]
list.append(1)
list.insert(0,1000000000000)
print(list)
print(len(list))

for a in list:
    if a % 2 == 0:
        print("{}는 짝수입니다.".format(a))
    else:
        print("{}는 홀수입니다.".format(a))
        

for element in list:
    print("{0}는 {1}자릿수입니다.".format(element,len(str(element))))
    
list1 = [1,2,3,4,5,1,11,1,2,2,3,4,7,457,347,1,5]
print(list1)
print(list1 + list)
print(list + list1)

list_of_list = [[6,2,5],[4,3,1,9],[8,7]]
list_a = []
#print(list_of_list[0][1])

i = 0
j = 0
k = 0
for list in list_of_list:
    for element in list:
         print(element)
         
for k in range(9):
    for i in range(len(list_of_list)):
        for j in range(len(list_of_list[i])):
            if k+1 == list_of_list[i][j]:
                print(list_of_list[i][j])
                print("{}{}".format(i,j))

                
#for k in (1:9):
    
        
numbers = [1,2,3,4,5,6,7,8,9]
output = [[],[],[]]

for number in numbers:
    output[(number +2 ) % 3].append(number)#어렵다#수식넣기
    
print(output)