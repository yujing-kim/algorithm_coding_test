# 해시 > 완주하지 못한 선수
def solution(participant, completion):
    p = {}
    for i in participant:
        if i not in p.keys(): p[i] = 1
        else: p[i]+=1
    for i in completion: p[i]-=1
    for k,v in p.items():
        if v != 0:
            answer = k   
    return answer