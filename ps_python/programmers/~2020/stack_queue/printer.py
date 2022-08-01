# 코딩테스트연습 > 스택큐 > 프린터

def solution(priorities, location):
    answer = 0 
    idx = [i for i in range(len(priorities))] # 대기열의 몇번째였는지
    z = list(zip(idx,priorities))
    while z:
        top = z.pop(0) # 대기열의 앞에것 제거
        flag = 0
        for i, p in z:
            if top[1] < p:
                flag = 1 # 대기열에 우선순위 높은 것이 있으면 flag=1
                break
        
        if flag == 1:
            z.append(top) # 우선 순위 높은게 있으면 뒤에 넣기
        else: # 아니면 인쇄
            answer+= 1
            if location == top[0]: # 내가 원하는 loc이면 return
                return answer

    return answer