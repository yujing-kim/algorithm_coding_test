
def solve(s):
    global ans # 바꾸어야 할 변수는 글로벌 선언
    for p in possible:
        now = s + str(p)
        ans = min(ans, len(now)+abs(n-int(now)))
        if len(now) < 6:
            solve(now)

n = int(input())
m = int(input())
ans = abs(n-100) # 100에서 +-만 눌러서 가는 방법
if m: # 고장난 버튼이 있는 경우
    broken = list(map(int, input().split()))
    # 고장나지 않은 버튼만 구하기 (set을 이용하자!)
    possible = set(i for i in range(10))-set(broken)
    solve('')
else: # 고장난 버튼이 없는 경우
    ans = min(ans, len(str(n)))


print(ans)
