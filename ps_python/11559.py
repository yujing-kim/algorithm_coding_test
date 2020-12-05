# 뿌요뿌요
import sys 
from copy import deepcopy
from collections import *
r = sys.stdin.readline

ans = 0
arr = [list(r().strip()) for i in range(12)] # 가장 중요한 부분 이었다..
# 문자열을 list 로 바꿀때는 strip()를 꼭꼭 사용하자
# arr = [list(r())[:-1] for i in range(12)] # 이렇게 했더니 런타임 에러..

def bfs(ty, tx, char):
    queue = deque([(ty,tx)])
    xylist = [(ty,tx)]
    while queue:
        ty, tx = queue.popleft()
        for dy, dx in [(0,-1),(0,+1),(-1,0),(+1,0)]:
            ny, nx = ty+dy, tx+dx
            if (0 <= ny < 12) and (0 <= nx < 6) and not ch[ny][nx] and arr[ny][nx] == char:
                ch[ny][nx] = 1
                queue.append((ny, nx))
                xylist.append((ny, nx))
    # 같은 것이 4개 이상이면 없애기
    global flag
    if len(xylist) >= 4:
        flag = True
        for xy in xylist:
            iy, ix = xy
            arr[iy][ix] = '.'

def drop():
    for i in range(6):
        col = deque([ arr[j][i] for j in range(12) if arr[j][i] != '.'])
        while len(col) != 12:
            col.appendleft('.')
        for j in range(12): # 결과 반영
            arr[j][i] = col[j]

flag = True
while flag == True:
    flag = False
    ch = [[0]*6 for _ in range(12)]
    # 터트리는 부분
    for y in range(12):
        for x in range(6):
            if arr[y][x] != '.' and not ch[y][x]:
                ch[y][x] = 1
                bfs(y, x, arr[y][x])
    # 연쇄 +1
    ans += 1
    # 중력에 의해 떨어뜨리는 부분
    drop()
    # down()
print(ans-1)
