# dfs/bfs > 게임 맵 최단거리 level2
from collections import deque

def solution(maps):
    answer = 1 # 첫번째 칸은 밟고 시작하므로
    r = len(maps) #row
    c = len(maps[0]) #col

    visited = [ [0 for _ in range(c)] for _ in range(r)] #방문배열
    dist = [ [0 for _ in range(c)] for _ in range(r)] #거리배열

    queue = deque([(0,0)]) # 큐 선언
    visited[0][0] = 1 # 방문 체크
    dist[0][0] = 1

    while queue :
        x,y = queue.popleft() # 좌표를 나누어 꺼내는 방법**
        for dx, dy in ((0,1), (0,-1), (1,0), (-1,0)):
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= r or ny < 0 or ny >= c: #범위 유효성 검사
                continue
            if visited[nx][ny] == 0 and maps[nx][ny] == 1: #방문한 적 없고, 밟을 수 있는 땅이면
                visited[nx][ny] = 1
                queue.append((nx,ny)) #바뀐 좌표를 넣기
                dist[nx][ny] = dist[x][y]+1 #이전 칸에 +1 하기

    return -1 if dist[-1][-1] == 0 else dist[-1][-1]


if __name__ == '__main__':
    maps = [
        [1,0,1,1,1],
        [1,0,1,0,1],
        [1,0,1,1,1],
        [1,1,1,0,1],
        [0,0,0,0,1]] # 답 11
    maps2 = [
        [1,0,1,1,1],
        [1,0,1,0,1],
        [1,0,1,1,1],
        [1,1,1,0,1]] # 
    print(solution(maps2))