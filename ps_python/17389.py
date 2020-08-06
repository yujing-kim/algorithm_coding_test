# 17389 보너스점수
n = int(input())
l = list(map(ord,list(input())))
# O(알파벳 대문자 O, ASCII 코드 79)와 X(알파벳 대문자 X, ASCII 코드 88)

b_flag = 1 # flag
bonus = 0
total = 0
for idx,i in enumerate(l,1):
    if i == 79:
        total = total + idx + bonus
        bonus += 1
    else:
        bonus = 0

print(total)
