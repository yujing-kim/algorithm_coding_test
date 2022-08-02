# 해시 _ 베스트엘범 _level3 (통과)
def solution(gen, play):
    # mulist = 장르 : [(재생수, 고유번호)]
    # total = 장르 : 총 재생수 
    answer, mulist, total = [], dict(), dict()
    g_len = len(gen) # 장르의 갯수

    for i in range(g_len) :
        if gen[i] in mulist: # 장르 key가 존재하면?
            mulist[gen[i]].append((play[i], i)) # (재생수, 고유번호)
            total[gen[i]] = total[gen[i]] + play[i] # 총 재생 수
        else : # 장르 key가 존재안하면?
            mulist[gen[i]] = [(play[i],i)]
            total[gen[i]] = play[i]
    
    # total 을 정렬 _ 재생수를 기준으로 내림차순 정렬
    total_sort_list = sorted(list(total.items()), key=lambda x :-x[1])

    for gen, j in total_sort_list:
        if len(mulist[gen]) == 1: # 조건1 ) 곡이 한개라면, 하나만 넣기 **
            answer.append(mulist[gen][0][1])
        else : 
            # 조건2 ) 재생 수가 같다면 고유번호 낮은 순 넣기 **
            mulist[gen].sort(key=lambda x:(-x[0], x[1])) 
            answer.append(mulist[gen][0][1])
            answer.append(mulist[gen][1][1])

    return answer

# 조금 수정해보기
def solution2(gen, play):
    answer, mulist, total = [], dict(), dict()

    for i, (g, p)  in enumerate(zip(gen, play)) : # enumerate와 zip을 사용하기 **
        if gen[i] in mulist: 
            mulist[g].append((p,i)) 
            total[g] += p # += 연산자 사용하기 **
        else : 
            mulist[g] = [(p,i)]
            total[g] = p
    
    for gen, j in sorted(total.items(), key=lambda x :-x[1]):
        for p, go in sorted(mulist[gen], key=lambda x:(-x[0], x[1]))[:2] :
            answer.append(go)
            

    # print(answer)
    return answer


if __name__ == '__main__':
    genres = ["classic", "pop", "classic", "classic", "pop"]	
    plays = [500, 2500, 150, 800, 2500]	
    solution(genres, plays)
    solution2(genres, plays)