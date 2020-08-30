# 정렬 > Hindex
def solution(cita):
    answer = []
    cita.sort(reverse = True) # 내림차순 정렬
    cita.append(0)
    answer = [ i for i in range(len(cita)) if i >= cita[i]]

    return answer[0]