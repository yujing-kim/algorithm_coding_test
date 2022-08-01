# 17204 죽음의 게임 _ 시뮬레이션
import sys
n, k = map(int, sys.stdin.readline().split())
arrow = [int(sys.stdin.readline()) for i in range(n)]

pick = arrow[0]
m = 1
while pick != k:
    pick = arrow[pick]
    m += 1
    n -= 1
    if n == 0:
        m = -1
        break

print(m)