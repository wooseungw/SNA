import sys


    

def DFS(node):
        
    #DFS
    
    while(stack):
        flag = stack.pop()
        
        if flag not in visited:
            visited.append(flag)
        else:
            continue
        
        for j in range(node,0,-1):
            if matrix[flag][j] == 1 and j not in visited:
                stack.append(j)
            
    print(len(visited)-1)     
    """ 
    for i in visited:
        print(i,end=' ')
    """


st_point = 1
node = sys.stdin.readline()
edge  = sys.stdin.readline()
node = int(node)
edge = int(edge)

visited = []
stack = [st_point]
matrix = []


#2차원 배열 생성
for i in range(node+1):
    matrix.append([])
    for j in range(node+1):
        matrix[i].append(0)
        
        if i == j and i!=0:
            matrix[i][j] = 1

for i in range(edge):
    
    temp_x,temp_y = sys.stdin.readline().split(" ")
    temp_x,temp_y = int(temp_x),int(temp_y)
    
    matrix[temp_y][temp_x] = 1    
    matrix[temp_x][temp_y] = 1    

for i in range(node+1):

    print(matrix[i])

DFS(node)