from typing import Any
class Queue:
    def __init__(self, size):
        self.size = size
        self.front = 0
        self.rear = 0
        self.queue = [ None for _ in range(size) ]
        
    def __str__(self) -> str:
        return str(self.queue)
    
    def isFull(self):
        if ( (self.rear + 1) % self.size == self.front) :
            return True
        else :
            return False
        
    def isEmpty(self):
        if (self.front == self.rear) :
            return True
        else :
            return False
        
    def enQueue(self, data):
        if (self.isFull()) :
            print("큐가 꽉 찼습니다.")
            return None
        # data는 튜플의 형태, 올바른 입력이 들어왔는지 확인
        if data[0] is not None and data[1] is not None and type(data[0]) == str and type(data[1]) == int:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data
        else:
            print("올바른 입력이 아닙니다.")
            return None
            
    def deQueue(self):
        if (self.isEmpty()):
            print("큐가 비었습니다.")
            return None
        self.front = (self.front + 1) % self.size
        data = self.queue[self.front]
        self.queue[self.front] = None
        return data
    
    def calTime(self):
        f = (self.front+1) % self.size
        r = (self.rear+1) % self.size
        if (self.isEmpty()):
            return 0
        timeSum = 0
        if r < f:
            for i in range(0, r):
                timeSum += self.queue[i][1]
            for i in range(f,(self.size)):
                timeSum += self.queue[i][1]
        else:
            for i in range(f, r) :
                timeSum += self.queue[i][1]
        return timeSum

if __name__ =="__main__":
    # 대기열 큐의 길이보다 많은 콜이 있고 중간에 첫번째 콜이 처리되는 경우
    waitCall = [('고장', 3), ('환불', 4), ('환불', 4), ('고장', 3), ('환불', 4), ('사용', 9)]
    SIZE = 6
    q = Queue(SIZE)
    i = 0
    for call in waitCall:
        i += 1
        print("귀하의 대기 예상시간은 ", q.calTime(), "분입니다.")
        print("현재 대기 콜 --> ", q)
        if i == 3:
            q.deQueue()
        q.enQueue(call)
        print()
    print("최종 대기 시간 --> ",q.calTime(),"분")
    print("최종 대기 콜 --> ",q)