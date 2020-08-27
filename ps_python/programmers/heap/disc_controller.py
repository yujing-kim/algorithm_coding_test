# 힙(heap) > 디스크컨트롤러
import heapq
def solution(jobs):
    answer, length = 0, len(jobs)
    heapq.heapify(jobs) # 최소 힙 정렬
    time = 0 # 시간
    
    while jobs: # 작업이 남아있음
        ch= [] # 작업을 잠시 담아둘 list
        
        # 현재 시간 이하인 경우 ch에 담기
        while jobs and jobs[0][0] <= time:
            p = heapq.heappop(jobs)
            ch.append(p)
        
        # solve
        # 1. 현재 시간에 해결할 수 있는 작업이 없음
        if len(ch) == 0:
            time += 1
            continue
        
        # 2. 작업이 있음
        ch.sort(key=lambda a :a[1], reverse = True) # 내림차순(뒤에서 빼기 위해)
        answer += time - ch[-1][0] + ch[-1][1] # 최소값을 더해주기
        time += ch[-1][1] # 시간이 지남
        ch.pop() # 해결한 작업은 pop
        for i in ch: # 아직 남은 작업 다시 넣기
            heapq.heappush(jobs, i)
                
        
    # [0,3], [2,6] 
    # 3-2+6 = 7  time-job[][0] + job[][1]
    
    return int(answer/length)