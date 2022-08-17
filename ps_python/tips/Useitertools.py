# -*- coding: utf-8 -*- 

from itertools import combinations, permutations
import sys
input = sys.stdin.readline
# print = sys.stdout.write

N, M = map(int,input().split()) # N까지의 자연수 중에서 M을 고르기
Narr = [i+1 for i in range(N)]

for i in combinations(Narr, M):
    print(i)
print(' ')
for i in permutations(Narr,M):
    print(i)