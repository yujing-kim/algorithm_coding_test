# CPU 시뮬레이션
import sys
r = sys.stdin.readline

opdict = {
    'ADD' : ['0000', '0'],
    'ADDC': ['0000', '1'],
    'SUB' : ['0001', '0'],
    'SUBC': ['0001', '1'],
    'MOV' : ['0010', '0'],
    'MOVC': ['0010', '1'],
    'AND' : ['0011', '0'],
    'ANDC': ['0011', '1'],
    'OR' : ['0100', '0'],
    'ORC': ['0100', '1'],
    'NOT' : ['0101', '0'],
    'MULT' : ['0110', '0'],
    'MULTC': ['0110', '1'],
    'LSFTL' : ['0111', '0'],
    'LSFTLC': ['0111', '1'],
    'LSFTR' : ['1000', '0'],
    'LSFTRC': ['1000', '1'],
    'ASFTR' : ['1001', '0'],
    'ASFTRC': ['1001', '1'],
    'RL' : ['1010', '0'],
    'RLC': ['1010', '1'],
    'RR' : ['1011', '0'],
    'RRC': ['1011', '1'],
}

def solve(l):
    opl = opdict[l[0]]
    ans = opl[0] + opl[1]
    # rD 결정 부분
    rd = bin(int(l[1]))[2:].zfill(3)
    # rA 결정 부분
    ra = bin(int(l[2]))[2:].zfill(3)
    # rb, c# 결정
    if opl[1] == '1' : # c#
        reg = bin(int(l[-1]))[2:].zfill(4)
    else:
        reg = bin(int(l[-1]))[2:].zfill(3) + '0'
    ans += ('0' + rd + ra + reg)
    print(ans)

N = int(r())
for n in range(N):
    solve(list(r().split()))
