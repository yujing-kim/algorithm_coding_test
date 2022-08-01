# 큰 상자에서 작은 상자 빼기
# 한번만 나오는 것은 긴변 
# 그 것부터 3개 뒤에 나오는 것이 작은 네모의 변

K = int(input())
arr = {}
# vector = []
l_list = []
for i in range(6):
    idx, l = map(int,input().split())
    # vector.append(idx)
    # l_list.append(l)
    l_list.append((idx, l))
    if idx not in arr.keys():
        arr[idx] = [l]
    else:
        arr[idx].append(l)
        

total, mins = 1, 1
for i in [1,2,3,4]:
    if len(arr[i]) == 1:
        total *= arr[i][0]
        min_idx = l_list.index((i, arr[i][0]))+3
        if min_idx > 5: min_idx = min_idx-6
        mins *= l_list[min_idx][1]

# print(total, mins)
print(( total - mins ) * K )
