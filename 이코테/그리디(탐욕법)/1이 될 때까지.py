n , k = map(int, input().split())

result = 0
## 최대한 많이 나누기
for i in range(n):
    if n % k == 0:
        n //=k
        result +=1
    else:
        n -=1
        result +=1
    if n == 1:
        break

print(result)