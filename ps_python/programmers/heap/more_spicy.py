# 코딩테스트연습 > 힙(heap) > 더 맵게
import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    
    for num in scoville:
        heapq.heappush(heap, num)
    
    # heapq.heapify(scoville)
    
    while heap[0] < K:
        if len(heap) == 1:
            return -1
        answer += 1
        s1, s2 = heapq.heappop(heap) ,heapq.heappop(heap) 
        heapq.heappush(heap, s1+(s2*2))
        
    return answer

# heap을 사용하여 push, pop 할때 정렬 해줌으로써 정렬 비용을 감소시킨다