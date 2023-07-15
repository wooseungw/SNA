import sys

def binary_search(list,i,left,right):
    mid = (left + right )//2
    
    if left >= right:
        print(check(list[left],i))
    else:
        if list[mid] == i:
            print(1)  
        elif list[mid] > i:
            binary_search(list,i,0,mid-1)
        elif list[mid] < i:
            binary_search(list,i,mid + 1,right)   

def check(buff,i):
    if(buff == i):
        return 1
    else:
        return 0

arr_len = int(sys.stdin.readline())

arr = sys.stdin.readline().split(" ")
arr = list(map(int,arr))

ans_len = int(sys.stdin.readline())

ans_ar = sys.stdin.readline().split(" ")
ans_ar = list(map(int,ans_ar))


#이진탐색을 통한 수 찾기
arr.sort()

for i in ans_ar:
    binary_search(arr,i,0,len(arr)-1)
        
    
    
        
        
        
