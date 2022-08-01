# 2484_주사위 네개_

# 1. 같은 눈이 4개 -> len 1
# 2. 같은 눈이 3개 -> len 2
# 3. 같은 눈이 2개씩 2쌍 -> len 2
# 4. 같은 눈이 2개만 -> len 2
# 5. 모두 다른 눈이 나오는 경우 -> len 4
def solve(dice, dice_sum):
    global money
    two, two_idx = 0, 0

    if len(dice) == 1:
        money = max(money, 50000+dice[0]*5000)
        return
    if len(dice) == 4:
        money = max(money, 100*max(dice))
        return
    for idx,i in enumerate(dice_sum):
        if i == 3:
            money = max(money, 10000+idx*1000)
            return
        if i == 2:
            two += 1
            two_idx = idx

    if two == 1:
        money = max(money, 1000+two_idx*100)
    else :
        money = max(money, 2000+sum(dice*500))

# 2 2 6 6  => 1000+3000+2000
# 6 2 1 5 => 600

import sys
T = int(sys.stdin.readline())
money = 0

for i in range(T):
    dice_sum = [0]*7 # 0으로 초기화 되는 6칸의 list 만들기
    dice = list() # unique한 주사위의 눈을 넣을 list

    for i in list(map(int, sys.stdin.readline().split())):
        dice_sum[i] += 1 # 나온 횟수를 넣음
        if i not in dice:
            dice.append(i) # 안에 없으면 집어넣음

    solve(dice, dice_sum)

print(money)
