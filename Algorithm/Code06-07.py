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

def peek():
    global SIZE,stack,top
    if(isStackEmpty ==True) :
        print('stack is empty')
        return None
    return stack[top]
    


def pop():
    global SIZE,stack,top
    if isStackEmpty == True :
        print('스택 텅')
        return 
    
    data = stack[top]
    stack[top]=None
    top -= 1
    return data


def push(data):
    global SIZE,stack,top
    if (isStackFull()):
        print('stack is full')
        return
    top += 1
    stack[top]=data



SIZE = 5
stack = [None,None,None,None,None]
top = -1

if __name__ == '__main__':

    select = input('삽입(I),추출(E),확인(V),종료(X) 중 하나를 선택 ==>')

    while(select!='X'):
        if select =='I':
            data = input('삽입할 데이터를 입력하세여==>')
            push(data)
            print("스택 상태",stack)

        elif select == 'E':
            data = pop()
            print('추출한 데이터: ', data)
            print("스택 상태",stack)
  

        elif select == "V":
            print(peek())
            print("스택 상태",stack)

        else :
            break

        select = input('삽입(I),추출(E),확인(V),종료(X) 중 하나를 선택 ==>')
        
