pasta1 = int(input(""))
pasta2 = int(input(""))
pasta3 = int(input(""))
juice1 = int(input(""))
juice2 = int(input(""))

list_pasta = [pasta1,pasta2,pasta3]
list_juice = [juice1,juice2]
list_set = []

for i in list_pasta:
    for j in list_juice:
        k = round((i+j)*1.1,1)
        list_set.append(k)

print(min(list_set))