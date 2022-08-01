# 16956 늑대와 양

def solve():
    # 전수 조사
    for i in range(R):
        for j in range(C):
            # 늑대를 만나면
            if maps[i][j] == 'W':
                # 울타리를 치자
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if nx < 0 or nx >= R or ny < 0 or ny >= C:
                        continue
                    if maps[nx][ny] == 'S' :
                        print(0)
                        return
                    else:
                        if maps[nx][ny] == '.': 
                            maps[nx][ny] = 'D'

                    # try:
                    #     if maps[nx][ny] == 'S' :
                    #         print(0)
                    #         return
                    #     else:
                    #         if maps[nx][ny] == '.': 
                    #             maps[nx][ny] = 'D'
                    # except IndexError:
                    #         continue
    print(1)
    for i in range(R):
        print(''.join(maps[i]))                     



R, C = map(int, input().split())
maps = [list(input()) for _ in range(R) ]
dx, dy = [0,0,1,-1], [-1,1,0,0]

solve()