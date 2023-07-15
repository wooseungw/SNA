import sys

queue = []
caseNum = int(sys.stdin.readline())
count = 0

print(len(queue))
def push(buff):
    queue.append(buff)
    
def pop():
    if len(queue)==0:
        print(-1)
    else:
        del queue[0]

def size():
    print(len(queue))

def empty():
    if len(queue)==0:
        print(-1)
    else:
        print(0)

def front2():
    if len(queue)==0:
        print(-1)
    else:
        print(queue[0])

def back2():
    if len(queue)==0:
        print(-1)
    else:
        print(queue(len(queue)-1))



for i in range(caseNum):
    
    command= sys.stdin.readline().split()
    
    if(command[0] == "push"):
        command[1] = int(command[1])
        push(command[1])
        count += 1        
    elif(command[0] == "pop"):
        pop()
        if(count >0):
            count -= 1
    elif(command[0] == "size"):
        size()
    elif(command[0] == "empty"):
        empty()
    elif(command[0] == "front"):
        front2()
    elif(command[0] == "back"):
        back2()
    
    