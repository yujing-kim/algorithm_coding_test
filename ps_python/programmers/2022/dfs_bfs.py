# dfs_bfs 연습하기

# dfs는 스택 구조로 동작 / 스택을 직접 사용하는 것이 아니고, 재귀함수를 이용
def dfs(graph, v, visited):
    visited[v]=True # v에 들어오면 방문표시한다.
    print(v, end=' ')
    for i in graph[v]: # v에 연결된 node를 탐색
        if not visited[i]: # 방문한 적이 없으면 방문하자
            dfs(graph, i, visited)


# bfs는 큐 자료구조를 사용
# 이때, collections모듈의 deque를 사용하는 것이 속도 면에서 좋다.

from collections import deque
def bfs(graph, start, visited):
    queue = deque([start]) # queue를 만든다.
    visited[start]=True # 방문 표시한다
    while queue : # queue가 비어지기 전까지 반복한다.
        v = queue.popleft() # 앞에서 제거
        print(v, end=' ') 
        for i in graph[v]: # 연결된 노드를 모두 큐에 넣으면서 방문한다.
            queue.append(i)
            visitied[i] = True

if __name__ == '__main__':
    graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
    ]

    visited = [False]*9
    dfs(graph, 1, visited)

    visited = [False]*9
    bfs(graph, 1, visited)

