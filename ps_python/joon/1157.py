import sys
from collections import Counter
input = sys.stdin.readline

word = list(str(input()).strip().upper())
most = Counter(word).most_common()

mx, le = 0, ''

if len(most) > 1 and most[0][1] == most[1][1]:
    print('?')
else :
    print(most[0][0])

# counter 사용하면 내림차순으로 정렬해줌 **

