from sys import *
setrecursionlimit(10 ** 6) # 재귀쓸때 꼭 있어야함..

def dfs(x, y, high):
    global check
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N :
            continue
        else:
            if arr[nx][ny] > high and not check[nx][ny]: # 안전지대이면서 아직 방문안함
                check[nx][ny] = 1
                dfs(nx, ny, high)
        

N = int(stdin.readline())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]

max_h= max(map(max, arr))
# print(max_h)

dx = [0,0,-1,+1]
dy = [-1,+1,0,0]

ans = []
for h in range(max_h+2):
    save = 0
    check = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not check[i][j] and arr[i][j] > h:
                check[i][j] = 1
                dfs(i, j, h)
                save += 1
    ans.append(save)

print(max(ans))
    


