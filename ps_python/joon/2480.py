import sys
sys.stdin = open("input.txt", "r")

num = list(map(int, sys.stdin.readline().split()))
check = list()
money, s = 0, 0

for i in num:
    if i in check:
        s = i
    if i not in check:
        check.append(i)

chlen = len(check)
if chlen == 1:
    money = 10000 + check[0] * 1000
elif chlen == 2:
    money = 1000+ s * 100
else:
    money = max(check) * 100

print(money)