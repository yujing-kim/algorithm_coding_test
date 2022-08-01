# 2484 _ 주사위 네개
from collections import Counter

ans = 0

for _ in range(int(input())):
    # dict 값
    dice_cnt, s = Counter(map(int, input().split())), 0
    two_cnt = list(dice_cnt.values()).count(2)
    for key, val in dice_cnt.items():
        if val == 4 :
            s += 50000+key*5000
            break
        elif val == 3 :
            s += 10000+key*1000
            break
        elif val == 2 :
            s += key*(500 if two_cnt==2 else 100)
    s += 2000 if two_cnt == 2 else 1000 if two_cnt == 1 else max(dice_cnt.keys())*100 if len(dice_cnt) == 4 else 0
    ans = max(ans, s)
print(ans)

