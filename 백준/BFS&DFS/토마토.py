import sys
from collections import deque
r = sys.stdin.readline


def bfs(M,N,box,queue):
    
    result= 0
    # 상하좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while queue:
        ##queu에 담긴 모든 익은 토마토의 상하좌우 경로 탐색
        for i in range(len(queue)):
            x, y = queue.popleft()
            ## 상하 좌우 탐색
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if (0 <= nx < N) and (0 <= ny < M) and (box[nx][ny] == 0):
                    box[nx][ny] = 1
                    queue.append((nx,ny))
        result +=1
    
    for i in box:
       if 0 in i:
           return -1
            
    return result -1


M, N = map(int, r().split())
box, queue = [], deque()
for i in range(N):
    row = list(map(int, r().split()))
    ## 입력 받을 때 익은 토마토의 위치를 queue에 담는다
    for j in range(M):
        if row[j] == 1:
            queue.append((i, j))
    box.append(row)


print(bfs(M,N,box,queue))




