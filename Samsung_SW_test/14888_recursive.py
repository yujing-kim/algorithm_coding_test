
def solve(res, cnt, add, sub, mul, div):
    global maxans, minans
    if cnt == n:
        maxans = max(maxans, res)
        minans = min(minans, res)
        return
    else:
        if add:
            solve(res+num[cnt], cnt+1, add-1, sub, mul, div)
        if sub:
            solve(res-num[cnt], cnt+1, add, sub-1, mul, div)
        if mul:
            solve(res*num[cnt], cnt+1, add, sub, mul-1, div)
        if div:
            solve(int(res/num[cnt]), cnt+1, add, sub, mul, div-1)

if __name__ == "__main__":
    n = int(input())
    num = list(map(int, input().split()))
    op = list(map(int, input().split()))
    minans, maxans = 100000001, -100000001
    solve(num[0],1,op[0],op[1],op[2],op[3])
    print(maxans)
    print(minans)