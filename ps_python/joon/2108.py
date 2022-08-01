# 통계학
# 산술평균 : 모든 값 더해서 나누기
# 중앙값
# 최빈값 : 가장 많이 나타나는 값
# 범위 : 최소값과 최대값의 차이
import collections
import sys
N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]


if N == 1:
    print(nums[0])
    print(nums[0])
    print(nums[0])
    print(0)
else:
    nums.sort()
    print(int(round(sum(nums)/N,0))) # 산술평균
    print(nums[N//2]) # 중앙값

    many = collections.Counter(nums).most_common(2) # 빈도수 상위 2개를 추출
    print(many[1][0] if many[0][1] == many[1][1] else many[0][0]) 
    print(nums[-1] - nums[0]) # 범위 

# 봐야할 부분
# collections.Counter 사용법
# 정렬 sort 사용법 -> 기본 오름차순

# nums.sort(key=lambda t : -t) # 내림차순 정렬법
