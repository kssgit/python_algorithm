## 키패드 문제 (시간 초과로 못품)
def solution(numbers, hand):
    answer = ''
    left = 0
    right = 0
    for number in numbers:
        if number in [1,4,7]:
            left = number
            print('1',answer)
            answer += 'L'
        elif number in [3,6,9]:
            right = number
            print('2',answer)
            answer +='R'
        else:
            if (left+1 ==right-1 == number and hand == 'left'):
                print('3',answer)
                answer +='L'
                
            elif left+1 ==right-1 == number and hand == 'right':
                print('4',answer)
                answer +='R'
                
            elif left+1 == number:
                print('5',answer)
                answer +='L'
                
            elif right-1 == number:
                print('6',answer)
                answer +='R'
        
    return answer

## 다른사람 풀이
# 절대값 구하는 함수 abs()
# 몫과 나머지를 tuple로 반환 함수 divmod(a,나누려는 값)
def solution1(numbers, hand):
    answer = ''
    lastL = 10
    lastR = 12
    
    for n in numbers:
        if n in [1,4,7]:
            answer+='L'
            lastL = n
        elif n in [3,6,9]:
            answer+='R'
            lastR = n
        else:
            n = 11 if n == 0 else n
            
            absL = abs(n-lastL)
            absR = abs(n-lastR)
            
            if sum(divmod(absL, 3)) > sum(divmod(absR, 3)):
                answer+='R'
                lastR = n
            elif sum(divmod(absL, 3)) < sum(divmod(absR, 3)):
                answer +='L'
                lastL = n
            else:
                if hand == 'left':
                    answer+='L'
                    lastL = n
                else:
                    answer+='R'
                    lastR = n
                
    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'left'
test=solution(numbers, hand)
print(test)
result ="LRLLLRLLRRL"