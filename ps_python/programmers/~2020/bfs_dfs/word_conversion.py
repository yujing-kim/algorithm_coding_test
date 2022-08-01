# dfs/bfs > 단어 변환
answer = 0
def solution(begin, target, words):
    global answer
    check = set()
    if target not in words: return 0 # target이 없음
    
    def bfs():
        global answer
        queue = [[begin, 0]]
        
        while queue:
            comp_word, cnt = queue.pop(0)
            for w in words: # 모든 word와 비교
                one = 0
                for i in range(len(begin)):
                    if comp_word[i] != w[i]:
                        one += 1
                if one == 1: # 한글자 다름
                    if w not in check:
                        if target == w: 
                            answer = cnt+1
                            return
                        queue.append([w,cnt+1])
                        check.add(w)       
    bfs()
    return answer