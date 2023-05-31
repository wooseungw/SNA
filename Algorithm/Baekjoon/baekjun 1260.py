import sys

  
def DFS(node,st_point):
    
    #순서 출력을 위한 list
    visited = []    
    #DFS
    
    stack = [st_point]
    
    while(stack):
        
        flag = stack.pop() #0번째는 st_point,그리고 그 이후는 matrix가 1일 때의 j값
        
        if flag not in visited:
            #현재 flag값이 출력될 list에 없으면 flag를 list에 추가하기
            visited.append(flag)
        
        for j in range(node,0,-1):
            #현재 줄에서 뒤에서 부터 탐색 visited에 없으면 stack에 추가하여 flag 변경
            if matrix[flag][j] == 1 and j not in visited:
                stack.append(j)
            

    #출력 제어문
    for i in visited:
        print(i,end=' ')


   
   
  
def BFS(node,st_point):
    
    queue = [st_point]
    visited = []    
    
    
    for i in queue:
        
        if len(queue) == len(elements):
            break
        else:
            for j in range(1,node+1):
                if j in queue:
                    continue
                else:
                    if matrix[i][j] == 1:
                        queue.append(j)
        
                
                         
                    
    for i in queue:
        print(i,end=' ')
      



node, edge, st_point = sys.stdin.readline().split(" ")
node = int(node)
edge = int(edge)
st_point = int(st_point)





matrix = []
#2차원 배열 생성
for i in range(node+1):
    matrix.append([])
    for j in range(node+1):
        matrix[i].append(0)
        
        if i == j and i!=0:
            matrix[i][j] = 1

x = []
y = [] 
elements = set()

for i in range(edge):
    
    temp_x,temp_y = sys.stdin.readline().split(" ")
    temp_x,temp_y = int(temp_x),int(temp_y)
    elements.add(temp_x)
    elements.add(temp_y)
    matrix[temp_y][temp_x] = 1    
    matrix[temp_x][temp_y] = 1    



print()   
for i in range(1, node+1):
    
    for j in range(1,node+1):
        print(matrix[i][j] ,end=" ")
    print()
print()       


   
#DFS
DFS(node,st_point)
  
print()
#BFS
BFS(node,st_point)

""" 
7 10 1
1 2
1 3
2 4
2 5
3 5
3 6
4 5
4 7
5 7
6 7 

8 7 1
1 4
1 2
2 3
2 7
7 8
4 3
3 5

10 9 1
1 2
1 3
2 4
4 8
4 9
3 5
3 6
3 7
7 10


15 14 1
1 2
1 3
2 4
2 5
3 6
3 7
4 8
4 9
5 10
5 11
6 12
6 13
7 14
7 15

DFS: 1 2 4 8 9 5 10 11 3 6 12 13 7 14 15
BFS: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15


"""