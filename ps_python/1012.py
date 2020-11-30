# 유기농 배추!
from collections import deque
def bfs(x, y):
    global check
    check[x][y] = 1
    queue = deque([(x,y)])
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    while queue:
        rx, ry = queue.popleft()
        for i in range(4):
            nx, ny = rx+dx[i], ry+dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            else:
                if not check[nx][ny] and arr[nx][ny] == 1:
                    check[nx][ny] = 1 # 방문
                    queue.append((nx, ny))        

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0]*M for i in range(N)]
    check = [[0]*M for i in range(N)]

    for k in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    # for i in range(len(arr)):
    #     print(arr[i])
    ans = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if check[i][j] == 0 and arr[i][j] == 1:
                bfs(i,j)
                ans += 1
    print(ans)
