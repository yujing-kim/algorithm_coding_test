# 거북이 시뮬레이션
# F: 한 눈금 앞으로
# B: 한 눈금 뒤로
# L: 왼쪽으로 90도 회전
# R: 오른쪽으로 90도 회전
import sys
r = sys.stdin.readline
def solve(l):
    x,y,s = 0,0,3 # s 방향 : 0,1,2,3(동남서북)
    lx , ly = [0], [0]
    for i in l :
        if i == 'F':
            if s == 0 : x += 1
            elif s == 1 : y -= 1
            elif s == 2 : x -= 1
            else : y += 1
        elif i == 'B':
            if s == 0 : x -= 1
            elif s == 1 : y += 1
            elif s == 2 : x += 1
            else : y -= 1
        elif i == 'L':  s = (s - 1)if s-1 >= 0 else 3
        elif i == 'R' : s = (s+1) if s+1 <= 3 else 0
        lx.append(x)
        ly.append(y)
    print( (max(lx)-min(lx))*(max(ly)-min(ly)) )

T = int(r())
for t in range(T):
    solve(list(r())[:-1])