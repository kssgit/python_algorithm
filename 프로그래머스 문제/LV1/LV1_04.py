## k번째수
## 정렬
def solution(array, commands):
    answer = []
    re = []
    for c in commands:
        re = array[c[0]-1:c[1]]
        re.sort()
        answer.append(re[c[2]-1])
    
    return answer


array =[1, 5, 2, 6, 3, 7, 4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]



## 다른 사람 풀이
# ??
def solution1(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

## 다른 사람 풀이 2
# sorted를 이용하는 방법
def solution2(array, commands):
    answer = []
    for i,j,k in commands:
        answer.append(sorted(array[i-1:j])[k-1])
    return answer

result = solution2(array,commands)
print(result)