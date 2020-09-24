from itertools import permutations
n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))
minans, maxans = 100000001, -100000001
# 연산자를 실체로
real_op = ['+']*op[0] + ['-']*op[1] + ['*']*op[2] + ['//']*op[3]

for permu in list(permutations(real_op, n-1)):
    res = num[0]
    for idx, opr in enumerate(permu,1):
        if opr == '+':
            res += num[idx]
        elif opr == '-':
            res -= num[idx]
        elif opr == '*':
            res *= num[idx]
        else:
            res = int(res / num[idx])
    minans = min(minans, res)
    maxans = max(maxans, res)
print(maxans)
print(minans)