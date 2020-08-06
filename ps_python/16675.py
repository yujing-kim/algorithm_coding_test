# 16675_두개의 손_구현_시뮬레이션_조건문
import sys
srp = list(sys.stdin.readline().split())
ms=srp[:2]
tk=srp[2:]
print(ms, tk)
# 0,1 : MS, 2,3: TK
# S R P 가위 바위 보
# S>P   R>S   P>R
# 1>0   2>1   0>2

# ss sp


if ms[0]=='S' and 'P' in tk:
    print(1)