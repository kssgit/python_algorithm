## 각 행마다 가장 작은 수를 찾은 후 
## 그뒤 가장 큰수를  찾는다
n , m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int , input().split()))
    data.sort()
    #min(data) 를 이용해서 최소 값 구하기
    if data[0] > result:
        result = data[0]


print(result)