# 2294.py - 동전2 - dp
n,k = map(int,input().split())
coin = []
dp = [0 for i in range(k+1)]
for _ in range(n):
    temp = int(input())
    if temp <= k:
        coin.append(temp)
        dp[coin[-1]] = 1

for idx in range(min(coin)+1,k+1):
    for c in coin:
        if 0 < idx-c and dp[idx-c] != 0:
            if dp[idx] == 0:
                dp[idx] = dp[idx-c]+1
            else:
                dp[idx] = min(dp[idx-c]+1, dp[idx])

print(dp[k] if dp[k]!= 0 else -1)
