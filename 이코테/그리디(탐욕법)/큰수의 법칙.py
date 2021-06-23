## 그리디 방법 사용

n , m , k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

ko = 0
answer = 0

for i in range(m):
    if ko == k :
        answer += second
        ko = 0
    else:
        answer += first
        ko +=1

print(answer)

## 가장 큰수가 더해지는 횟수 계산
## 반복되는 수열에 대해서 파악해야 함
count = (m//(k+1))*k
count +=m%(k+1)

result = 0
result += (count)*first
result += (m-count)*second