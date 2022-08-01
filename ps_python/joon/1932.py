# 1932.py _ 정수 삼각형 _ dp
n = int(input())
tri, dp = [0], [0]

for i in range(n):
    l = list(map(int, input().split()))
    tri += zip(l, [i+1]*len(l))
    dp += l

for i in range(1,len(tri)-tri[-1][1]):
    idx = i + tri[i][1]
    dp[idx] = max(dp[i] + tri[idx][0], dp[idx])
    dp[idx+1] = max( dp[i] + tri[idx+1][0], dp[idx+1])

print(max(dp))

# 1 -> 2 3 n+1 # 줄의 idx를 더해주면 자식 노드
# 2 -> 4 5 n+2
# 3 -> 5 6 n+2
# 4 -> 7 8 n+3
# 5 -> 8 9 n+3
# 6 -> 9 10 n+3

#    1
#   2 3
#  4 5 6
# 7 8 9 10 

# 5
#     7          7
#    3 8       10 15
#   8 1 0     18 16 15
#  2 7 4 4   20 ...
# 4 5 2 6 5 