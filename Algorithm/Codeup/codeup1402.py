n = int(input())
list_input = input().split(" ")
list = list(map(int, list_input))
list2=[]
for i in range(len(list)):
    list2.append(list[n-i-1])

print(list2)