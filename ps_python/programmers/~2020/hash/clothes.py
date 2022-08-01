# 해시 > 위장
def solution(clothes):
    answer = 1
    c_dict = {}
    for c in clothes: # 옷의 갯수를 세어준다 종류별로
        if c[1] in c_dict.keys():
            c_dict[c[1]] += 1
        else:
            c_dict[c[1]] = 1
    
    for c in c_dict.values():
        answer *= (c+1) # 고르지 않는 경우를 포함하기 위해 1을 더한 후 곱해준다
    
    return answer-1 # 하나도 안입은 경우는 빼준다