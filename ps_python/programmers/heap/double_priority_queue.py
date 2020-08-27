# 힙(heap) > 이중우선순위큐

import heapq
def solution(operations):
    answer = []
    
    heap = []
    # flag = 0 # 0: 최소힙, 최대힙
    
    for op in operations:
        if op.split()[0] == 'I': # 삽입
                heapq.heappush(heap, int(op.split()[1]))
        else:
            if len(heap) == 0:
                continue
            if op.split()[1] == '-1':
                heapq.heappop(heap) #최소힙이라 그냥 뺀다
            else: # 최대값을 찾아서 빼고 다시 힙정렬한다.
                heap.remove(max(heap))
                heapq.heapify(heap)

    if len(heap) == 0: # heap이 비어있음
        answer = [0,0]
    else: # 힙이 비어있지 않음
        answer.append(max(heap))
        answer.append(min(heap))
             
    return answer