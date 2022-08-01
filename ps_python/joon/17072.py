# 17072 아스키 아트 _ 구현
import sys
n, m = map(int,sys.stdin.readline().split())
# 행, 열
answer=list()

for i in range(n):
    answer_l = list() # 행 배열
    temp_rgb = list(map(int, sys.stdin.readline().split()))
    for j in range(0,len(temp_rgb),3):
       a = temp_rgb[j:j+3] # 3개씩 자르기
       i_rgb = 2126*a[0] + 7152*a[1] + 722*a[2] # 주어진 식을 대입
       if i_rgb < 510000 :
           answer_l.append('#')
       elif i_rgb < 1020000 :
           answer_l.append('o')
       elif i_rgb < 1530000 :
           answer_l.append('+')
       elif i_rgb < 2040000 :
           answer_l.append('-')
       else :
           answer_l.append('.')
    answer.append(answer_l)

for i in answer:
    print(''.join(i))
