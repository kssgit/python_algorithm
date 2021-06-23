n = int(input())
plans = input().split()

x, y =1 ,1

dy = [0,0,-1,1]
dx = [-1, 1, 0 , 0]
move_types = ['L','R','U','D']

for p in plans:
    a = move_types.index(p)
    nx= x+dx[a]
    ny= y+dy[a]
    if nx <1 or nx > n or ny <1 or ny >5:
        continue
    x, y = nx, ny

print(y,' ',x)
            