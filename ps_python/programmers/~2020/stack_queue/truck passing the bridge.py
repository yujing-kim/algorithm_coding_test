# 코딩테스트연습 > 스택/큐 > 다리를 지나는 트럭

def solution(bridge_length, weight, truck_weights):
    answer = 0
    ing = [] # 건너고 있는 트럭
    sum_w = 0 # 건너고 있는 트럭의 총 합
    
    while truck_weights:
        answer+=1 # 1초 증가

        if sum_w+truck_weights[0] <= weight:
            sum_w += truck_weights[0]
            ing.append([truck_weights.pop(0),0]) # (트럭무게, 0초) 넣기

        flag = 0 # 다리를 모두 건넌 트럭이 있음!
        # 모두 1초 늘려주기 (다리 길이만큼인 것은 빼고)
        for idx, i in enumerate(ing) :
            if i[1]+1 != bridge_length:
                i[1]+=1
            else:
                sum_w-=i[0]
                flag = 1
        if flag == 1: ing.pop(0) # 건넌것은 제거해주기

    return answer+bridge_length