# 완전탐색 > 모의고사
def solution(answers):
    math1 = [1,2,3,4,5]
    math2 = [2,1,2,3,2,4,2,5]
    math3 = [3,3,1,1,2,2,4,4,5,5]

    t1, t2, t3 = 0, 0, 0
    answer = []
    # 시험은 최대 10000문제
    # 여러명이 답인 경우에는 오름차순 출력

    for idx, a in enumerate(answers):
        if a == math1[idx%5]:
            t1 += 1
        if a == math2[idx%8]:
            t2 += 1
        if a == math3[idx%10]:
            t3 += 1
    m = max(t1,t2,t3)
    for idx, t in enumerate([t1,t2,t3],1):
        if t == m:
            answer.append(idx)

    return answer