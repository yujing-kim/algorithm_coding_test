# 124나라의 숫자
def solution(n):
    answer = ''
    if n <= 3:
        return '124'[n-1]
    else:
        q,r = (n-1)//3, (n-1)%3 
        # 다른 진법과 다르게 0이 없다. 즉 앞 수의 124진법(3으로 나누어 구하는 수)을 구한것이 이번수의 124수이다.
        return solution(q)+'124'[r]