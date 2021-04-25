def isQueueFull():
    global SIZE, queue, front,rear
    if rear == SIZE-1:
        
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
    rear +=1 
    queue[rear]=data

def deQueue():
    global SIZE, queue, front,rear
    #front와 rear가 같다면 queue 가 비어있다
    if isQueueEmpty == True:
        print("queue is empty")
        return 
    front+=1
    data=queue[front]
    queue[front]=None
    return data

def peek():
    global SIZE, queue, front,rear
    if isQueueEmpty ==True:
        print("queue is empty")
        return 
    return queue[front+1]

SIZE = 5

# queue = [None for _ in range(SIZE)]
# front = rear = -1
queue = ['화사',None,None,None,None]
front = -1
rear = 3

print(queue)
retData = deQueue()
print('추출 -->',retData)
retData = deQueue()
print('추출 -->',retData)
print(queue)



