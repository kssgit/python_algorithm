# 원형 큐 (대용량의 값들을 다룰 때 5000개 이상)

def isQueueFull():
    global SIZE, queue, front,rear
    if (rear+1)%SIZE == front:
        return True
    else:
        return False


def isQueueEmpty():
    global SIZE, queue, front,rear
    if rear == front:
        
        return True
    else:
        return False
    
def enQueue(data):
    global SIZE, queue, front,rear
    if isQueueFull() == True:
        print("queue is full")
        return None
    rear =(rear+1)%SIZE 
    queue[rear]=data

def deQueue():
    global SIZE, queue, front,rear
    #front와 rear가 같다면 queue 가 비어있다
    if isQueueEmpty == True:
        print("queue is empty")
        return 
    front = (front+1)%SIZE
    data=queue[front]
    queue[front]=None
    return data

def peek():
    global SIZE, queue, front,rear
    if isQueueEmpty ==True:
        print("queue is empty")
        return 
    return queue[(front+1)%SIZE]

SIZE = 5

# queue = [None for _ in range(SIZE)]
# front = rear = -1
queue = [None,None,"문별","휘인","선미"]
front = 1
rear = 4

if __name__ == "__main__":
    select = input('삽입(I),추출(E),확인(V),종료(X) 중 하나를 선택 ==>')

    while(select != "x" or select!="X"):
        if select =="I" or select=="i":
            data = input('삽입할 데이터 ==>')
            enQueue(data)
            print(queue)
            
        elif select=="E" or select=="e":
            data =deQueue()
            print('추출한 데이터 ==>',data)
            print(queue)

        elif select == "V" or select=="v":
            print(peek())
            print(queue)
        else:
            break
        select = input('삽입(I),추출(E),확인(V),종료(X) 중 하나를 선택 ==>')
