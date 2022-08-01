import copy
n, m = map(int,input().split())
arr = []
ans = []
for ni in range(n):
    arr.append(list(input()))

for x in range(n-7):
    for y in range(m-7):
        cnt1, cnt2 = 0 , 0
        c1 = [arr[x+i][y:y+8] for i in range(8)]
        c2 = copy.deepcopy(c1)

        # 흰색으로 시작
        if c1[0][0] == 'B':
            cnt1 = 1
            c1[0][0] = 'W'
        for i in range(7):
            for j in range(7):
                if c1[i][j] == 'W':
                    if c1[i+1][j] == 'W':
                        c1[i+1][j] = 'B'
                        cnt1 += 1
                    if c1[i][j+1] == 'W':
                        c1[i][j+1] = 'B'
                        cnt1 += 1 
                if c1[i][j] == 'B':
                    if c1[i+1][j] == 'B':
                        c1[i+1][j] = 'W'
                        cnt1 += 1
                    if c1[i][j+1] == 'B':
                        c1[i][j+1] = 'W'
                        cnt1 += 1
        if (c1[7][7] == c1[7][6]) or (c1[7][7] == c1[6][7]):
            cnt1+=1
        
        # 검은색으로 시작
        if c2[0][0] == 'W':
            cnt2 = 1
            c2[0][0] = 'B'
        for i in range(7):
            for j in range(7):
                if c2[i][j] == 'W':
                    if c2[i+1][j] == 'W':
                        c2[i+1][j] = 'B'
                        cnt2 += 1
                    if c2[i][j+1] == 'W':
                        c2[i][j+1] = 'B'
                        cnt2 += 1 
                if c2[i][j] == 'B':
                    if c2[i+1][j] == 'B':
                        c2[i+1][j] = 'W'
                        cnt2 += 1
                    if c2[i][j+1] == 'B':
                        c2[i][j+1] = 'W'
                        cnt2 += 1
        if (c2[7][7] == c2[7][6]) or (c2[7][7] == c2[6][7]):
            cnt2+=1
        ans.append(min(cnt1, cnt2))
print(min(ans))
# print(ans)