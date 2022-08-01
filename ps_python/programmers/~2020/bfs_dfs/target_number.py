# 깊이너비우선 > 타겟넘버
answer, nums, tar = 0,[],0 # 전역
def solve(idx,sum):
    global answer # 바꿀 값
    if sum == tar and len(nums) == idx:
        answer+=1
        return
    if idx == len(nums) : return
    
    for i in [-1,1]:
        solve(idx+1,sum+nums[idx]*i)
    return
            

def solution(numbers, target):
    
    global answer, nums, tar # 바꿀 값
    answer, nums, tar = 0, numbers, target 
    solve(0,0) 

    return answer