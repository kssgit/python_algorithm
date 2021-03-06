## 완주하지 못한 사람
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for par , comp in zip(participant, completion):
        if par !=comp:
            #동명이인 값 
            return par
    return participant.pop()


participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

result = solution(participant,completion)
print(result)

## 다른 사람 풀이
import collections
## collections 모듈을 이용한 객체 빼기

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


## 다른 사람 풀이 (해시 사용)
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
