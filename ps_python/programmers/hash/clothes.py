# 해시 > 위장
def solution(clothes):
    answer = 1
    c_dict = {}
    for c in clothes:
        if c[1] in c_dict.keys():
            c_dict[c[1]] += 1
        else:
            c_dict[c[1]] = 1
    
    for c in c_dict.values():
        answer *= (c+1)
    
    return answer-1