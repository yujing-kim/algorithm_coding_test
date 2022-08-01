# 전기줄 - dp
# 선을 최소로 없애서 겹치지 않게 하라
# 즉, 선이 겹치지 않는 최대의 집합을 구하는 것입니다.

N = int(input())
arr = [list(map(int ,input().split())) for _ in range(N)] # 입력 받음

arr.sort(key=lambda t : t[0]) # 앞의 원소로 정렬

dest = [0]*501 # 전체 인덱스에 대한 배열

for i,j in arr:
    dest[j] = max(dest[:j])+1 # 현재 가리키는 인덱스까지의 수 중에서 최대값에 1을 더합니다.
print(N - max(dest))