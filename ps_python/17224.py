# 17224 _ APC는 왜 서브태스크 대회가 되었을까?
import sys

ans = 0 # 답
sub = list() # 문제 리스트

n, l, k = map(int,sys.stdin.readline().split()) # 문제수, 능력치, 풀이가능갯수
for i in range(n): # 문제 난이도 입력
    pro = list(map(int, sys.stdin.readline().split()))
    sub.append(pro)

sub.sort(key=lambda x:x[1]) # 두번째 원소로 정렬

for i in range(n):
    if k <= 0: # 더이상 문제를 못풂
        break
    if sub[i][1] <= l: # sub2를 풀수 있으면 140점
        ans += 140
        k-=1
        continue
    if sub[i][0] <= l: # sub1만 풀수 있으면 100점
        ans += 100
        k-=1
        continue

print(ans)