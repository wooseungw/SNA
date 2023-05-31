# |이 코드는 몸무게와 키를 입력받아 몸무게를 기준으로 내림차순 정렬한 후, 각 사람의 등수를 구하는 코드입니다.
# |
# |좋은 점:
# |- 입력받은 데이터를 리스트에 저장하여 처리하는 방식으로, 데이터 관리가 용이합니다.
# |- 몸무게를 기준으로 내림차순 정렬하는 부분에서, sort() 함수를 사용하는 대신 sort(reverse=True)를 사용하여 코드를 간결하게 작성하였습니다.
# |
# |나쁜 점:
# |- weight와 height 변수를 리스트로 선언하였지만, 이후에 입력받은 값을 각각 weight와 height 변수에 덮어쓰는 실수가 있습니다. 이를 방지하기 위해서는 다른 변수명을 사용하거나, weight와 height를 이차원 리스트로 선언하여 각각의 값을 저장해야 합니다.
# |- sort_weight 변수에 weight.sort(reverse=True)를 대입하였지만, sort() 함수는 원본 리스트를 정렬하고 None을 반환하므로, sort() 함수를 사용한 후에는 sort() 함수를 대입하지 않아야 합니다.
# |- while문에서 len(rank)이 n보다 작을 때까지 반복하도록 설정하였지만, rank 리스트에 추가되는 값이 n보다 작을 경우 무한루프에 빠질 수 있습니다. 이를 방지하기 위해서는 while문의 조건을 len(rank) < n으로 변경해야 합니다.
import sys
weight =[]
height =[]
n = int(sys.stdin.readline())

rank = []

for i in range(n):
    weight, height = list(map(int,sys.stdin.readline().split()))

print(weight)
print(height)

sort_weight = []

sort_weight = weight.sort(reverse=True)

#몸무게 정렬 후 번호 부여할것 정렬 

print(sort_weight)
#이차원 배열이라 인덱스값이 하나가 아님
k = 0
while(len(rank)<= n):
    if(sort_weight.index(weight[k])):#data의 값과 sortdata값을 비교후 같으면 sortdata의 index 리턴
        k = 0
        rank.append(sort_data.index(data[0][k]))
    else:
        k = k + 1
         
    
print(rank)