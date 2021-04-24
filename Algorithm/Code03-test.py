katok=[]

def add_data(friend):
    katok.append(None)
    klen = len(katok)
    katok[klen-1]=friend

def insert_data(position,friend):
    katok.append(None)
    klen=len(katok)

    for i in range(klen-1,position,-1):
        katok[i]=katok[i-1]
        katok[i-1]=None

    katok[position]=friend

def delet_data(position):

    klen=len(katok)
    katok[position]=None
    for i in range(position+1,klen,1):
        katok[i-1]=katok[i]
        katok[i]=None

    del(katok[klen-1])

if __name__=="__main__":
    select=-1
    while(select!=4):
        select=int(input("선택하세요(1: 추가,2:삽입,3:삭제,4:종료)-->"))

        if (select==1) :
            name=input("추가할 데이터 -->")
            add_data(name)
            print(katok)
        elif (select==2):
            position=input("삽입할 위치-->")
            name=input("추가할 데이터 -->")
            insert_data(position,name)
            print(katok)
        elif (select==3):
            position=input("삭제할 위치-->")
            delet_data(position)
            print(katok)