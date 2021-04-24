katok=['다현', '정현', '쯔위', '사나', '지효']

def delet_data(position):

    klen=len(katok)
    katok[position]=None
    for i in range(position+1,klen,1):
        katok[i-1]=katok[i]
        katok[i]=None

    del(katok[klen-1])


delet_data(2)
print(katok)
delet_data(3)
print(katok)
