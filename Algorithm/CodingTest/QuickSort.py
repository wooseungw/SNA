#파티션은 pivot보다 큰 왼쪽index와 pivot보다 작은 오른쪽 index의 value를 swap
#

def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and pivot <= arr[right]:
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
            
    arr[start], arr[right] = arr[right], arr[start]
    return right


def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot - 1)
        quick_sort(arr, pivot + 1, end)
    return arr




def Swap(list,left,right):
    temp = list[left]
    list[left] = list[right]
    list[right] = temp

def Partition3(list,left,right):
    
    low_index = left + 1
    high_index = right
    
    pivot = list[left]
    done = False
    while not done:
        while (list[low_index] <= pivot and low_index <= high_index):
            low_index += 1
        while(list[high_index] >= pivot and low_index <= high_index):
            high_index -= 1
            
        if(low_index > high_index):
            done = True
        else:
            Swap(list,low_index,high_index)
        
        Swap(list,left,high_index)
            
        
        
    
    
    return high_index


def QuickSort3(list, left,right):
    
    if(left<right):
        pivot = Partition3(list,left,right)
        QuickSort3(list,left,pivot-1)
        QuickSort3(list,pivot+1,right)
    
    
    return 0

list = [5,4,3,2,6,7,8,9,1]

print(len(list))
print(list[8])
print(list[0])

quick_sort(list,0,len(list)-1)

print(list)




def Partition2(list,left,right):
    #low,high는 index값이다.
    low = left - 1
    high = right + 1   
    
    pivot = list[left] #피벗은 각 list의 첫 항
    while(True):#do while 형태의 반복문 피벗 왼쪽의 인덱스 > 우측의 인덱스크기 이면 멈춘다.
        
        while(True):#low는 왼쪽에서 오른쪽으로 탐색해가다가 피벗보다 큰 데이터를 찾으면 멈춘다.
            
            if(low <= right and list[low]<pivot): #low의 값이 list인덱스의 끝값보다 같거나 작을때,list[low]가 pivot보다 작으면
                low += 1
                continue
            else:
                break
        
        while(True):#high는 오른쪽에서 왼쪽으로 탐색해가다가 피벗보다 작은 데이터(2)를 찾으면 멈춘다.
            
            if(left >= high and list[high]>pivot):
                high -=1
                continue
            else:
                break
        
        if(low < high):#low와 high가 (교차하지 않고 while문 2개를 빠져나오면) == (list low가 피벗보다 크고, list[high]는 피벗보다 작은 것이 된다.)  list값을 swap , if문의 조건이 불필요한 swap을 막는다. 
            Swap(list,low,high)
        
        if(low>=high):#do-while loop종료를 위한 if문
            break

    Swap(list,low,high) #교차한 경우 swap
    
    return high

def Quicksort2(list,left,right):
    

    if(left<right):
        
        pivot_index = Partition2(list,left,right)
        
        Quicksort2(list,left,pivot_index)
        
        Quicksort2(list,pivot_index+1,right)  

    return 0
