def isStackFull():
    global SIZE,stack,top
    if (top >=SIZE-1) :
        return True
    else:
        return False

def isStackEmpty():
    global SIZE,stack,top
    if top==-1:
       return True
    else:
        return False

 
def push(data):
    global SIZE,stack,top
    if (isStackFull()):
        print('stack is full')
        return
    top += 1
    stack[top]=data


def pop():
    global SIZE,stack,top
    if isStackEmpty == True :
        print('스택 텅')
        return 
    
    data = stack[top]
    stack[top]=None
    top -= 1
    return data


SIZE = 5
stack = ['커피',None,None,None,None]
top = 0

print(stack)
retData=pop()
print('추출데이터 ==>',retData)
retData=pop()
print('추출데이터 ==>',retData)

