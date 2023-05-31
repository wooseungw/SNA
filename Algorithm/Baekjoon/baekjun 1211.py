numbers = [20,1,12,9,18]

for i in numbers:
    print("{}   {}".format(i,"*"*i))
    
list1 = [1,2,3,4,5,6]
list2 = [6,7,8,9,10]

for i in list1:
    for e in list2:
        if i == e:
            print("True")
            break
        
list = int(input(numbers))