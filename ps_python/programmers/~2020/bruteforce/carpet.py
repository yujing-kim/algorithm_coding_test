# 완전탐색 > 카펫
def solution(brown, yellow):
    answer = []
    if yellow == 1 : return [3,3]
    else:
        for i in range(1, yellow//2+1):
            if yellow%i == 0:
                if brown == (i+yellow//i)*2 + 4:
                    return [i+2,yellow//i +2] if i > yellow//i else [yellow//i+2, i+2]