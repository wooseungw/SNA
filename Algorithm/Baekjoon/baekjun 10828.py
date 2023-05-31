import sys

def push(list,num):
    list.append(num)
    
def pop(list,index):
    if index >0:    
        print(list.pop())
    else:
        print(-1)
    
def size(list):
    print(len(list))

def empty(list,index):
    if index > 0:
        print(0)   
    else:
        print(1)

def top(list,index):
    if index > 0:
        print(list[index - 1])
    else:
        print(-1)
    
command = []
list = []
count = 0    

    
case_num = int(sys.stdin.readline().strip())

for i in range(case_num):
    
    command= sys.stdin.readline().split()    

    if(command[0] == "push"):
        command[1] = int(command[1])
        push(list,command[1])
        count += 1        
    elif(command[0] == "pop"):
        pop(list,count)
        if(count >0):
            count -= 1
    elif(command[0] == "size"):
        size(list)
    elif(command[0] == "empty"):
        empty(list,count)
    elif(command[0] == "top"):
        top(list,count)
    
    

