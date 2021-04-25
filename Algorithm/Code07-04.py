def isQueueFull():
    global SIZE, queue, front,rear
    if rear == SIZE-1:
        
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










SIZE = 5

# queue = [None for _ in range(SIZE)]
# front = rear = -1
queue = ['화사','솔라','문별','휘이',None]
fornt = -1
rear = 3

print(queue)
enQueue('선미')
print(queue)
enQueue('재남')
print(queue)

