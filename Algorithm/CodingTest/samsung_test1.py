import sys


a_boom = []
b_boom = []
c_boom = []

fp = open("CodeTest\input1.txt","r")

def bomb_a(a_boom):
    lens = len(a_boom)/2
    grid_num = 0
    i=0
    for i in range(int(lens)):
        
        x = int(a_boom[grid_num] )
        y = int(a_boom[grid_num+1])#입력이 안됨.
        grid_num = grid_num+2
        
        matrix[x][y] = 1
        
        # if(x>0):
        #     matrix[x-1][y] = 1
        # if(x<len(matrix[0])):
        #     matrix[x+1][y] = 1
        # if(y>0):
        #     matrix[x][y-1] = 1    
        # if(y<len(matrix[0])):
        #     matrix[x][y+1] = 1
            
    for p in matrix:
        print(p)

case_num = fp.readline()
case_num = case_num.strip()
for i in range(int(case_num)):
    map_size = fp.readline()
    map_size = map_size.strip()
    
    global matrix
    x=0
    y=0
    matrix = [[0 for x in range(int(map_size))] for y in range(int(map_size))]
    
    for p in matrix:
        print(p)
    
    buff = fp.readline()
    buff = buff.strip()
    
    buff = buff.split(',')
    for h in range(3):
        buff[h] = buff[h].strip()#개행문자 제거
    
    
    print(buff)
    
    a_boom = buff[0]
    a_boom = a_boom.split()
    b_boom = buff[1]
    b_boom = b_boom.split()
    c_boom = buff[2]
    c_boom = c_boom.split()
    
    bomb_a(a_boom)
    
    
    
    buff = "\000"


                
        
        
        
        
         
        

fp.close

