# bfs/dfs 타겟넘버 level2
answer = 0

def dfs_solve(num, tar, idx, now):
    # 1. 타겟 값과 같으며, 모든 숫자를 쓴 경우, answer하나를 추가
    # 2. 타겟 값과 같지않고, 모든 숫자를 쓴 경우, 그냥 return
    # 3. 타겟 값과 같지 않고, 숫자를 다 안쓴 경우 > 다음것 진행
    # 4. 타겟 값과 같고, 숫자를 다 안쓴 경우 > 다음것 진행
    global answer
    if tar == now and len(num) == idx : 
        answer += 1
        return
    if len(num) == idx : 
        return
    
    for i in [-1,1]:
        dfs_solve(num, tar, idx+1, now + num[idx]*i)
    return

def solution(num, tar):
    
    dfs_solve(num, tar, 0, 0 )
    print(answer)

    return answer

if __name__ == '__main__':
    numbers = [1,1,1,1,1]
    target = 3
    solution(numbers, target)
