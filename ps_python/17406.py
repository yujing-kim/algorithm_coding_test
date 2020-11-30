from itertools import permutations
from copy import deepcopy
def arrsum(array):
    global answer
    s = 6000
    for row in array:
        s = min(sum(row), s)
    answer.append(s)

def rotat(k):
    global array
    r,c,s = k
    ltop, rdown = [r-s-1, c-s-1], [r+s-1, c+s-1]
    while ltop != rdown:
        im = array[ltop[0]][ltop[1]]
        for r in range(ltop[1]+1, rdown[1]+1):
            tmp = array[ltop[0]][r]
            array[ltop[0]][r] = im
            im = tmp
        for c in range(ltop[0]+1, rdown[0]+1):
            tmp = array[c][rdown[1]]
            array[c][rdown[1]] = im
            im = tmp
        for r in range(rdown[1]-1, ltop[1]-1, -1):
            tmp = array[rdown[0]][r]
            array[rdown[0]][r] = im
            im = tmp
        for c in range(rdown[0]-1, ltop[0]-1, -1):
            tmp = array[c][ltop[1]]
            array[c][ltop[1]] = im
            im = tmp
        ltop[0]+=1
        ltop[1]+=1
        rdown[0]-=1
        rdown[1]-=1 # 다음 좌표 

N, M, K = map(int, input().split())
arr = [ list(map(int, input().split())) for n in range(N)]
answer = []

# 연산의 리스트
klist = [list(map(int, input().split())) for i in range(K)]
perm = list(permutations(klist,K)) # 경우의 수

# K 만큼 연산을 합니다.
for per in perm:
    array = deepcopy(arr)
    for p in per:
        rotat(p)
    arrsum(array) # 배열의 값을 구합니다.
print(min(answer))