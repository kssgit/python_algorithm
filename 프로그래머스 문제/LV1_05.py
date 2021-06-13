# 체육복 ( 못 풀었다)
def solution(n, lost, reserve):       
    answer = 0
    ge = {}
    for i in range(n):
        if i+1 in reserve:
            ge[i+1] = 2
            if i+1 in lost:
                ge[i+1] = 1
        else:
            if i+1 in lost:
                ge[i+1] = 0
            else:
                ge[i+1] = 1     

    print(ge)
    for i in lost:
        if i ==1 :
            if ge[i+1] == 2:
                ge[i] =1
                ge[i+1] = 1
        if i == n :
            if ge[i-1] ==2:
                ge[i] =1
                ge[i-1] =1
        elif ge[i-1] ==2:
            ge[i] =1
            ge[i-1] =1
        else:
            if ge[i+1] == 2:
                ge[i] =1
                ge[i+1] = 1 

    print(ge)
    for i in range(n):
        if ge[i+1] >1:
            answer +=1
        else:
            answer +=ge[i+1]
    return answer


n = 3
lost = [3]
reserve = [1]
## 다른 사람 문제 풀이 (그리디 알고리즘 )
# 출처 : https://rain-bow.tistory.com/entry/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%B2%B4%EC%9C%A1%EB%B3%B5
def solution1(n, lost, reserve): 
    set_reserve=set(reserve)-set(lost) 
    set_lost = set(lost)-set(reserve) 
    for i in set_reserve: 
        if i-1 in set_lost: 
            set_lost.remove(i-1) 
        elif i+1 in set_lost: 
            set_lost.remove(i+1) 
    return n-len(set_lost)

print(solution1(n,lost,reserve))