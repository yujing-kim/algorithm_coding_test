n = int(input())
cons, dp, end_dict = [0], [0], {}
for i in range(1,n+1):
    tmp = list(map(int,input().split()))
    cons.append(tmp)
    dp.append(0)
    if tmp[0]+i-1 > n:
        continue
    if tmp[0]+i-1 in end_dict.keys():
        end_dict[tmp[0]+i-1].append(i)
    else:
        end_dict[tmp[0]+i-1] = [i]

# print(cons,'\n',dp,'\n',end_dict)
for i in range(1,n+1):
    dp[i] = dp[i-1]
    if i in end_dict.keys():
        for j in end_dict[i]:
            dp[i] = max(dp[i], cons[j][1] + (dp[j-1] if j-1 > 0 else 0))
    else:
        dp[i] = dp[i-1]
print(dp[-1])