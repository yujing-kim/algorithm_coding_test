# 16675_두개의 손_구현_시뮬레이션_조건문
import sys
srp = list(sys.stdin.readline().split())

ms= ''.join(srp[:2])
tk= ''.join(srp[2:])
# print(ms, tk)

# 상대방이 같은 것을 낸 경우에만 이길 수 있다.
# win_dict = {
#     'SS' : 'PP',
#     'PS' : ['PP','RR']
#     'RS' : ['SS','PP']
#     'PR' : ['RR','PP']
#     'RR' : 'SS',
#     'PP' : 'RR',
# }

win_dic = {
    'S' : 'P',
    'P' : 'R',
    'R' : 'S'
}
flg = 0
for i in range(2):
    if win_dic[ms[i]]*2 == tk :
        print('MS')
        flg = 1
        break
    if win_dic[tk[i]]*2 == ms :
        print('TK')
        flg = 1
        break

if flg == 0:
    print('?')