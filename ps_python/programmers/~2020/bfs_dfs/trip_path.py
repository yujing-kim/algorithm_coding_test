# dfs/bfs > 여행경로
import copy
def dfs(num, dpath, ans, check, tickets):
        if check == [1]*len(tickets):
            ans.append(copy.deepcopy(dpath))
            return
    
        for idx, p in enumerate(tickets): # 티켓 탐색
            if check[idx]==0 and p[0]==tickets[num][1]:
                dpath.append(p[1]) # path에 추가
                check[idx] = 1
                dfs(idx, dpath, ans, check,tickets)
                dpath.pop() # 백트래킹
                check[idx] = 0

def solution(tickets):
    answer, check = [], [0]*len(tickets)
    
    for i in range(len(tickets)): # 티켓 갯수만큼 돌린다
        path, check = [], [0]*len(tickets)
        if tickets[i][0] == "ICN" and check[i] == 0: # 방문 아직안한 인천티켓으로 시작
            path += tickets[i]
            check[i] = 1
            dfs(i, path, answer, check,tickets)
    answer.sort()
    return answer[0]