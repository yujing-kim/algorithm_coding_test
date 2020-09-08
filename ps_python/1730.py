# 1730 판화 
n, m = int(input()), list(input())
ud = [[0 for _ in range(n)] for _ in range(n) ] # 수직 방향 
rl = [[0 for _ in range(n)] for _ in range(n) ] # 수평 방향

loc = [0,0]

# (x,y) (nx,ny) 가 수직관계이면 ud에 표시, 수평방향이면 rl에 표시
for i in m:
    x,y = loc
    if i == 'U' and x-1 >= 0:
        ud[x][y], ud[x-1][y] = 1,1
        loc = [x-1, y]
    elif i == 'D' and x+1 < n:
        ud[x][y], ud[x+1][y] = 1,1
        loc = [x+1, y]
    elif i == 'R' and y+1 < n:
        rl[x][y], rl[x][y+1] = 1,1
        loc = [x,y+1]
    elif i == 'L' and y-1 >= 0:
        rl[x][y], rl[x][y-1] = 1,1
        loc = [x,y-1]

# 수직 수평 다 지나갔으면 '+', 안지나 갔으면 '.'
for i in range(n):
    for j in range(n):
        if ud[i][j]+rl[i][j] == 2:
            print('+', end='')
        elif ud[i][j] == 1:
            print('|', end='')
        elif rl[i][j] == 1:
            print('-', end='')
        else:
            print('.',end='')
    print('')