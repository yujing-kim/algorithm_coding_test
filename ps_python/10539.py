# 10539 수빈이와 수열 _구현_누적합
n = int(input()) # 원소 갯수 입력
l = list(map(int, input().split())) # list입력

l = [i*idx for idx, i in enumerate(l,1)] # 전체 곱하기

print(l[0], end=' ')
for i in range(1,n):
    # print(i)
    print(l[i] - l[i-1], end=' ')


# 1    2    2      3       4
# 1 2*2:4 2*3:6  3*4:12  4*5:20
# 1    4-1   6-4   8-8    20-12
# 1     3    2      6        8

