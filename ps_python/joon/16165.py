# 16165.py _ 걸그룹마스터준석이
import sys

n, m = map(int,sys.stdin.readline().split()) # n : 답의 갯수 , m: 문제의 갯수

girl_dict = dict() # 걸그룹정보를 list로 만들어 dict로 넣기
reverse_dict = dict() # 걸그룹 멤버 : 그룹이름 넣기 (value에서 key를 찾기 위함)
                            # 속도는 빠르지만 메모리를 낭비한다는 단점
mem_list = list() # 각 그룹의 멤버를 담을 list -> 초기화 필수

# 답을 입력받음
for i in range(n):
    group = sys.stdin.readline().rstrip() # 그룹이름
    people = int(sys.stdin.readline()) # 멤버수
    for j in range(people):
        a = sys.stdin.readline().rstrip() # 개행문자를 제거할 수 있다
        mem_list.append(a)
        reverse_dict[a] = group # 반대로도 저장
    mem_list.sort() # 사전순 정렬
    girl_dict[group] = mem_list # dict에 리스트 넣기
    mem_list = [] # 초기화


# 문제를 내고 답을 출력한다.
for i in range(m):
    prob = sys.stdin.readline().rstrip() # 문제
    prob_num = int(sys.stdin.readline()) # 문제 유형
    if prob_num == 0: # 맴버를 출력
        for mem in girl_dict[prob] :
            print(mem)
    if prob_num == 1: # 그룹 이름을 출력
        print(reverse_dict[prob])
