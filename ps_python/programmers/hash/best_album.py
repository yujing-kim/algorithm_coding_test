# 프로그래머스 > 코딩테스트 연습 > 해쉬 > 베스트앨범

def solution(genres, plays):
    answer = []
    dic = dict()
    gen = dict()
    for idx, g in enumerate(genres):
        if g in dic.keys():
            dic[g].append((idx, plays[idx]))
            gen[g]+=plays[idx]
        else:
            dic[g] = [(idx,plays[idx])]
            gen[g] = plays[idx]
    # print(dic, gen)
    
    # 장르별 곡의 재생횟수 정렬
    for i in dic.values():    
        i.sort(key=lambda a:a[1], reverse=True)
    # print(dic)
    
    # 장르별로 정렬
    gen = dict(sorted(gen.items(), key=lambda a:a[1], reverse = True)).keys()
    # print(gen)
    
    
    # 장르별 곡이 한개인 경우는 하나만, 여러개인 경우는 2개의 고유번호 뽑기
    for g in gen:
        print(dic[g])
        if len(dic[g]) == 1:
            answer.append(dic[g][0][0])
        else:
            answer.append(dic[g][0][0])
            answer.append(dic[g][1][0])
            
    
    
    print(answer)
    # for i in plays:
    return answer