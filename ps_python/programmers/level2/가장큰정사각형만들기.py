def solution(board):
    answer = 0
    if len(board) == 1 or len(board[0]) == 1: # 세로로 긴 경우
        return 1
    for y in range(1,len(board)):
        for x in range(1,len(board[0])):
            if board[y][x] != 0: # 그 값이 0이 아닌 경우에 
                board[y][x] = min(board[y-1][x], board[y][x-1], board[y-1][x-1])+1
                answer = max(answer, board[y][x])
								# 위, 왼쪽, 대각선 의 값들 중에 최소값 + 1 
   
    return answer*answer