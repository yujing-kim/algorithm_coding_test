# 15953 _ 상금헌터
m17 = [
    (1 ,500),
    (3, 300),
    (6, 200),
    (10, 50),
    (15, 30),
    (21, 10)
    ]
m18 = [
    (1,512),
    (3,256),
    (7,128),
    (15,64),
    (31,32)
]

import sys
T = int(sys.stdin.readline()) # test case 갯수

for k in range(T):
    money = 0
    img17, img18 = map(int, sys.stdin.readline().split())
    for i, j in m17:
        if img17 == 0:
            break
        if img17 <= i:
            money+= j
            break
    for i, j in m18:
        if img18 == 0:
            break
        if img18 <= i:
            money+= j
            break
    print(money*10000)

