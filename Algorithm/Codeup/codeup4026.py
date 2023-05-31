
list_input = input().split(" ")
list = list(map(int, list_input))
list.sort(reverse=True)
list_odd = [0]
list_even = [0]

for i in list:
    if i % 2 == 0:
        list_even.append(i)
    elif i % 2 == 1:
        list_odd.append(i)

list_even.sort(reverse=True)
list_odd.sort(reverse=True)

print(list_even[0]+list_odd[0])