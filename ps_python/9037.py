# 9037.py _ The candy war _ 시뮬레이션
def is_same(list):
    for i in range(0,len(list)-1):
        if list[i] != list[i-1]:
            return 0



import sys

cycle = 0 # 순환

t = int(sys.stdin.readline())
child = int(sys.stdin.readline())
ch_li = list(map(int, sys.stdin.readline().split()))

# while not is_same(ch_li):
    # 홀수이면 채워주기
    for i in range(len(ch_li)):
        if ch_li[i]%2
ch_li = [i+1 for i in ch_li if i%2]
cycle+=1



print(ch_li)
print(cycle)

