num = int(input())
dong = []
grade = []
for n in range(num):
    
    kg, cm = map(int, input().split())
    dong.append([kg, cm])

for n in range(num):
    cnt = 0
    for j in range(num):
        if dong[n][0] < dong[j][0] and dong[n][1] < dong[j][1]:
            cnt += 1
    grade.append(cnt+1)

for i in grade:
    print(i, end=' ')
print('')