# 해시 _ 폰켓몬 (통과)
def solution(nums):
    answer = dict() # 딕셔너리
    for key in nums:
        if key not in answer:
            answer[key] = 1
        else :
            answer[key] = answer[key] + 1
    kinds = len(answer.keys())
    want = len(nums)//2

    return kinds if want >= kinds else want

# 다른 풀이
# set함수를 잊지말자!
def solution2(nums):
    return min(len(set(nums)), len(nums)//2 )


if __name__ == '__main__':
    nums = [3,3,3,2,2,2]
    solution(nums)
    solution2(nums)