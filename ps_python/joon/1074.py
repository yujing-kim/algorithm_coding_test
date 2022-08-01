# 1074 _ Z _구현_ 분할정복

import sys
n, r, c = map(int, sys.stdin.readline().split()) # 입력

# 0 1
# 2 3
ans = 0
while n > 0:
    area = (2**n)//2
    if n > 1:
        if area > r and area <= c: #1
            ans += area ** 2
            c-= area
        elif area <= r and area > c: #2
            ans += (area ** 2)*2
            r -= area
        elif area <= r and area <= c: #3
            ans += (area ** 2)*3
            r -= area
            c -= area
    elif n == 1:
        if r == 0 and c == 1:
            ans += 1
        elif r == 1 and c == 0:
            ans += 2
        elif r == 1 and c == 1:
            ans += 3
    n-=1
print(ans)



