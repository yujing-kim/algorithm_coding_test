
def sumsum(x1, y1, x2, y2):
    total = 0
    for x in range(x1, x2+1): # 세로로 더하기
        if y1 == 0:
            total += arr[x][y2]
        else:
            total += (arr[x][y2] - arr[x][y1-1]) # 가로의 합들을
    print(total)

N, M = map(int,input().split())
arr = [] # 배열
for i in range(N):
    row = []
    for r in list(map(int,input().split())):
        if row:
            row.append(row[-1]+r)
        else:
            row.append(r)
    arr.append(row)

K = int(input()) # 구간의 갯수
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    sumsum(x1-1, y1-1, x2-1, y2-1) # 배열의 좌표로 바꾸어줌