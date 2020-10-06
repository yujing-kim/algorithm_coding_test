# 스킬트리
def solution(skill, skill_trees):
    answer = 0 
    for st in skill_trees:
        skill_list = list(skill) # skill을 리스트로 만들기
        for s in st:
            if s in skill and skill_list: # skill에 있는 s를 만남
                if s != skill_list.pop(0): # 앞에 것과 다르다면 선행할것이 남은것
                    break
        else: # for-else구문
            answer+=1
    return answer