# 14620_꽃길


n = int(input()) # 한변
maps = [list(map(int, input().split())) for _ in range(n)] # 땅의 가격들
dx,dy = [-1,1,0,0,0], [0,0,-1,1,0]
answer = 50000 # 최대는 200*10*10

def solve(lst):
    flower = [] # 꽃이 차지하는 좌표를 모두 담을 것임
    money = 0
    
    for i in lst:
        x = i //n
        y = i % n

        if 0 == x or x == n-1 or y == 0 or y == n-1 :
            return 50000
        for d in range(5):
            nx, ny = x+dx[d],y+dy[d] 
            flower.append((nx,ny))
            money += maps[nx][ny]
    if len(set(flower)) == 15: # set 으로 만들었을 때 중복되는 것이 있으면 불가능
        return money
    else : return 50000
         

# 모든 경우를 해본다 ()
for i in range(n*n):
    for j in range(i+1,n*n):
        for k in range(j+1, n*n):
            answer = min(answer , solve([i,j,k]) )

print(answer)







