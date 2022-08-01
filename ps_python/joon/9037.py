# 9037.py _ The candy war _ 시뮬레이션
def is_same(list): # 값이 모두 같은가?
    for i in range(0,len(list)-1):
        if list[i] != list[i-1]:
            return 0
    return 1

def solve(ch_li):
    global cycle
    while not is_same(ch_li):
        # 마지막 원소 앞에 넣어주기
        ch_li.insert(0, ch_li[child - 1])
        next = [ch_li[i - 1] / 2 + ch_li[i] / 2 for i in range(1, len(ch_li))]
        cycle += 1
        ch_li = next

        # 홀수이면 채워주기
        for i in range(len(ch_li)):
            if ch_li[i] % 2:
                ch_li[i] += 1
        # print(next)
    return cycle


import sys

cycle = 0 # 순환(답)

t = int(sys.stdin.readline())


for i in range(t):
    child = int(sys.stdin.readline())  # 아이들 수
    ch_li = list(map(int, sys.stdin.readline().split()))

    # 홀수이면 채워주기
    for i in range(len(ch_li)):
        if ch_li[i] % 2:
            ch_li[i] += 1

    solve(ch_li)
    print(cycle)
    cycle = 0


