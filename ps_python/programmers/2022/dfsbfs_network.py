# 2022.08.04 네트워크 dfsbfs level3
import sys
from collections import deque
input = sys.stdin.readline


############################### 처음 작성한 코드 (통과) ###############################
global visited, graph
def bfs(idx):
    global visited, graph
    visited[idx] = True
    q = deque([idx])

    while q :
        fr = q.popleft()
        for e in graph[fr]:
            if visited[e] == False :
                q.append(e)
                visited[e] = True
    return

def solution(n, comp):
    global visited, graph

    answer = 0

    visited = [False for _ in range(n)]
    graph = [ [] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if comp[i][j] == 1 and i != j:
                graph[i].append(j)
                graph[j].append(i)

    # print(graph)

    for i in range(n):
        if visited[i] == False:
            bfs(i)
            answer += 1


    print(answer)
    return

if __name__ == '__main__':
    n = int(input())
    computers = [list(map(int, input().split())) for _ in range(n)]
    solution(n, computers)

##############################################################################

# 다시 작성한 코드 (통과)
n = int(input())
computers = [list(map(int, input().split())) for _ in range(n)]

answer = 0
visited = [False]*n # 방문 배열 
# graph 따로 만들지 않고 그냥 주어진 배열로 edge판단 가능

def bfs(idx):
    visited[idx] = True
    q = deque([idx])

    while q :
        fr = q.popleft()
        for e in range(n):
            if visited[e] == False and computers[e][fr] :
                q.append(e)
                visited[e] = True
    return

for i in range(n):
    if visited[i] == False:
        bfs(i)
        answer += 1


print(answer)