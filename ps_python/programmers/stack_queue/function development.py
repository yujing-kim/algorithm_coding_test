# 코딩테스트연습 > 스택/큐 > 기능개발
import math

def solution(progresses, speeds):
    answer = []
    q = []
    
    # 걸리는 일수를 계산하여 넣기
    for i in range(len(progresses)):
        days = (100-progresses[i]) / speeds[i]
        q.append(math.ceil(days))

    # 하나씩 빼면서 pub <= i 동안 원소 제거(한루에 pub 가능한 양)
    while q:
        pub = q.pop(0) # 오늘 내보낼 기능 : pub
        cnt = 1
        while q and q[0] <= pub: # 원소가 존재하고 pub <= 인경우 배포가능
            print(q)
            q.pop(0)
            cnt+=1
        answer.append(cnt)
    return answer