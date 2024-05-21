# 버블 정렬 함수
# arr: 정렬할 리스트
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# 선택 정렬 함수
# arr: 정렬할 리스트
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# 사용 예시
arr = [64, 34, 25, 12, 22, 11, 90]
selection_sort(arr)
print("정렬된 배열:", arr)
# 사용 예시
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("정렬된 배열:", arr)

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    merged_arr = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged_arr.append(left[l])
            l += 1
        else:
            merged_arr.append(right[r])
            r += 1
    
    merged_arr += left[l:]
    merged_arr += right[r:]
    return merged_arr

arr = merge_sort([64, 34, 25, 12, 22, 11, 90])
print("정렬된 배열:", arr)
def heap_sort(arr):
    # 힙을 유지하는 함수
    def heapify(arr, n, i):
        largest = i  # 루트를 가장 큰 요소로 초기화
        l = 2 * i + 1  # 왼쪽 자식
        r = 2 * i + 2  # 오른쪽 자식

        # 왼쪽 자식이 존재하고 루트보다 크다면
        if l < n and arr[i] < arr[l]:
            largest = l

        # 오른쪽 자식이 존재하고, largest보다 크다면
        if r < n and arr[largest] < arr[r]:
            largest = r

        # largest가 루트가 아니라면, 교환
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            # 교환 후에도 힙을 유지
            heapify(arr, n, largest)

    n = len(arr)

    # 최대 힙을 만듦
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # 하나씩 요소를 추출하면서 힙을 유지
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 현재 루트를 배열의 끝으로 이동
        heapify(arr, i, 0)  # 힙을 유지

    return arr
arr = heap_sort([64, 34, 25, 12, 22, 11, 90])
print("정렬된 배열:", arr)