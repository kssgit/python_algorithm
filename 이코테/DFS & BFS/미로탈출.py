## BFS

from collections import deque
n ,m = 5,6

graph = [
    [1,0,1,0,1,0],
    [1,1,1,1,1,1],
    [0,0,0,0,0,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]
]

def solution(graph,n,m):
    queue = deque()
    queue.append((0,0))
    # 상하 좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]


    while queue:
        x,y = queue.popleft()
        # 상하 좌우 모두 탐색
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            ##nx,ny 값이 graph의 index값을 넘어가면 continue
            if nx <0 or nx >= n  or ny <0 or ny >= m:
                continue
            ## 해당 좌표가 0이면 continue
            if not graph[nx][ny]:
                continue
            ## 해당 그래프의 값을 이전 방문의 graph 값의 +1을 해서 count를 센다
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] +1
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(solution(graph,n,m))
