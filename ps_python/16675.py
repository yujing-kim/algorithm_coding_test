# 16675_두개의 손_구현_시뮬레이션_조건문
import sys
srp = list(sys.stdin.readline().split())
ms= srp[:2].sort()
tk= srp[2:].sort()
print(ms, tk)
# 0,1 : MS, 2,3: TK
# S R P 가위 바위 보 -> sort : PRS
# S>P   R>S   P>R
# 1>0   2>1   0>2

win_dict = {
    'SS' : 'PP',

}

# 가위가위  가위보 가위바위 바위보     바위바위  보보       1이 낼 수 있는 경우의 수
# 보 보     보 보  가위가위 바위바위   가위가위  바위바위   이렇게 내면 1이 무조건 이김


# if ms[0]=='S' and 'P' in tk:
#     print(1)