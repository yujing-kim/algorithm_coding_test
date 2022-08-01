# 1920
import sys

n = int(sys.stdin.readline())
l = set(map(int,sys.stdin.readline().split()))
# print(l)

num = int(sys.stdin.readline())
num_l = list(map(int,sys.stdin.readline().split()))
# print(num_l)

for i in num_l:
    if i in l:
        print(1)
    else :
        print(0)
