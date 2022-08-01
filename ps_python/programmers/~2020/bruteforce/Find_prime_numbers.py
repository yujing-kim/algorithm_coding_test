# 완전 탐색 > 소수찾기
from itertools import permutations
import math

def check(n):
    if n == 0 or n == 1: # 0,1 은 소수아님
        return False
    for i in range(2, n//2+1): # 무언가로 나누어 지면 소수임
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    num_list = list(numbers) # 문자열을 list로!
    
    for l in range(1,len(num_list)+1): # 각 길이만큼 순열 만들기
        # 중복 제거 -> 문자열,정수로 변환 -> list로 변환
        p = list(map(int,map(''.join, set(permutations(num_list,l))))) 
        answer += [li for li in p if check(li)]
    
    return len(set(answer))

# 1. 소수를 구하는 방법 : 2~ n//2 까지 나누어 보았을 때, 안나뉘어 지면 소수이다.
# 2. 0,1 은 소수가 아닙니다.
# 3. 순열 구하기 → permutations 사용하기 → 인자 : (list, 순열길이)
# 4. 중복되는 숫자가 있으므로 순열을 구한 후, 중복을 제거해준다.