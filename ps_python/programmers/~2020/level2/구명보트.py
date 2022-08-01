def solution(people, limit):
    answer = 0 # 답
    people.sort(key= lambda x:-x) # 내림차순 정렬
    x, y = 0, len(people) - 1 # 인덱스
    while x <= y: 
        answer += 1 # 구출 한번
        if people[x]+people[y] <= limit: # 둘를 더해서 limit를 넘지 않으면
            y -= 1 # 작은 것도 구출하자
        x += 1 # 큰것은 무조건 구출하자
    return answer