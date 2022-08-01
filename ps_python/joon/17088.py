# 등차수열변환
# 각 숫자에 할 수 있는 연산은  [-1, 0, 1] 이렇게 세개 뿐이다.
# 첫번째와 두번째에 연산을 하고 나머지는 공차가 같아야한다!! -> 어렵다 이런걸 어떻게 생각하나?ㅠㅠ

def check(one, two):
    gap, change = two - one, 0
    new_arr = [one + gap * i for i in range(len(arr))]
    for i in range(len(arr)):
        c = abs(arr[i] - new_arr[i])
        if c > 1:
            return False, 0
        elif c == 1:
            change += 1
    return True, change


N = int(input())
arr = list(map(int,input().split()))
ans = 100000

if N == 1:
    print(0)
    exit()

for i in [-1,0,1]: # 경우는 9가지
    for j in [-1,0,1]:
        # 앞의 두 수를 조작해주고, 가능한지 체크한다.
        flag, cnt = check(arr[0]+i, arr[1]+j) # -> True/False, change cnt
        if flag:
            ans = min(ans, cnt)
print(ans if ans != 100000 else -1)
