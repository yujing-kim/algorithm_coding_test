# dfs/bfs > 네트워크
def dfs(idx, n, check,computers):
    for i in range(n):
        if check[i] == 0 and computers[idx][i] == 1:
            check[i] = 1
            dfs(i,n,check,computers)

def solution(n, computers):
    answer = 0
    check =[0]*n # 방문
    
    for idx in range(n):
        if check[idx] == 0:
            check[idx] = 1
            dfs(idx,n,check,computers)
            answer += 1
    return answer