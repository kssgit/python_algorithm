## 최단 경로 구하기
from collections import deque
n , k = map(int, input().split())

queue = deque()
queue.append((n-1,n+1,n*2,0))

def bfs(k):
    s = 0
    while queue:
        li = queue.popleft()
        if k in li[:3]:
            break
        else:
            for i in li[:3]:
                queue.append((i-1,i+1,i*2,li[-1]+1))
        s = li[-1] +1
    return s

print(bfs(k))
