import sys


num = -1 
board = []
check = []

def make_buff():
    global num
    num += 1
    if num < 25:
        return check[num]
    
def check_binggo():
    
    for i in range(5):
        
        if i == 2:
            for j in range(5):
                if board[i][j] == 0 and board[i-2][j] == 0 and board[i-1][j] == 0 and board[i+1][j] == 0 and board[i+2][j] == 0:
                    
                    return 1
                
                if j ==2:
                    if board[i][j] == 0 and board[i-1][j+1] == 0 and board[i-2][j+2] == 0 and board[i+1][j-1] == 0 and board[i+2][j-2] == 0 or board[i][j] == 0 and board[i-1][j-1] == 0 and board[i-2][j-2] == 0 and board[i+1][j+1] == 0 and board[i+2][j+2] == 0:
                        return 1
                    
        else:
            j = 0
            if board[i][j] == 0 and board[i][j-2] == 0 and board[i][j-1] == 0 and board[i][j+1] == 0 and board[i][j+2] == 0:
                return 1
                

for i in range(5):
    board.append([])

for i in range(5):
    board[i] = sys.stdin.readline().split(" ")
    board[i] = list(map(int,board[i]))

for i in range(5):
    check += list(map(int,sys.stdin.readline().split()))

print(board)
print()
print(check)


buff = make_buff()
i = 0
j = 0
count = 0
while num < 25:
    
        if j <= 3:
            j += 1
        else: 
            
            j = 0
            
            if i <= 3:
                i += 1
            else:    
                i = 0
    
    
        
        if buff == board[i][j]:
            board[i][j] = 0
            buff = make_buff()
            
            i = 0
            j = 0
        
        
        
        
        
        if check_binggo() == 1:
            
            count += 1  
            if count == 3:
                print(num+1)  
                break
            
           

        






