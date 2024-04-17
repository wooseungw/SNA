## 전역 변수 선언 부분 ##
SIZE = 1
while SIZE < 2:
    SIZE = int(input("큐의 크기를 입력하세요.:"))
queue = [ None for _ in range(SIZE) ]
front = rear = 0
num = 0
## 함수 선언 부분 ##
def isQueueFull() :
	global SIZE, queue, front, rear
	if ( (rear + 1) % SIZE == front) :
		return True
	else :
		return False

def isQueueEmpty() :
	global SIZE, queue, front, rear
	if (front == rear) :
		return True
	else :
		return False

def enQueue(data) :
	global SIZE, queue, front, rear
	if (isQueueFull()) :
		print("큐가 꽉 찼습니다.")
		return
	rear = (rear + 1) % SIZE
	queue[rear] = data

def deQueue() :
	global SIZE, queue, front, rear
	if (isQueueEmpty()) :
		print("큐가 비었습니다.")
		return None
	front = (front + 1) % SIZE
	data = queue[front]
	queue[front] = None
	return data

def peek() :
	global SIZE, queue, front, rear
	if (isQueueEmpty()) :
		print("큐가 비었습니다.")
		return None
	return queue[(front + 1) % SIZE]

def calcTime() :
	global SIZE, queue, front, rear
	timeSum = 0
	for i in range((front+1)% SIZE, (rear+1)%SIZE) :
		timeSum += queue[i][1]
	return timeSum

def print_queue():
    global SIZE, queue, front, rear
    print("현재 대시 시간 -->",calcTime(),"분")
    print("현재 대기 콜 --> ", queue)

while(num != 4):
    num = int(input("\n1.등록하기, 2.조회하기, 3.제거하기, 4:종료 -->"))
    if num == 1:
        call = input("콜 내용을 입력하세요.(1.사용, 2.고장, 3.환불, 4.기타):")
        if call == "1" or call == "사용":
            call = "사용"
            time = 9
        elif call == "2" or call == "고장":
            call = "고장"
            time = 3
        elif call == "3" or call == "환불":
            call = "환불"
            time = 4
        elif call == "4" or call == "기타":
            call = "기타"
            time = 1
        else: 
            print("잘못 입력하셨습니다! 다시 입력해주세요!", end = " ")
            continue
        enQueue((call, time))
        print_queue()
    elif num == 2:
        print_queue()
    elif num == 3:
        deQueue()
        print_queue()
    elif num == 4:
        break

    

print("프로그램 종료!")

