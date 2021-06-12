# 크레인 인형 뽑기 게임

def solution(board, moves):
    answer = 0
    stack = []
    for x in moves:
        for y in range(len(board)):
            #board 값이 0이 아니라면
            if board[y][x-1] !=0:
                #stack에 board 값 추가
                stack.append(board[y][x-1])
                #선택된 board 값 0으로 초기화
                board[y][x-1] = 0
                #stack에 2개 이상 값이 있을 경우 비교
                if len(stack)>1:
                    if stack[len(stack)-2] == stack[len(stack)-1] :
                        stack.pop()
                        stack.pop()
                        answer +=2
                break
    return answer

board = [
    [0,0,0,0,0],
    [0,0,1,0,3],
    [0,2,5,0,1],
    [4,2,4,4,2],
    [3,5,1,3,1]]

moves = [1,5,3,5,1,2,1,4]

result = solution(board,moves)

print(result)