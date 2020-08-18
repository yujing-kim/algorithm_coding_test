# 16769 _ Mixing Milk
# 세 개의 버킷이 있다.
# 첫번째 버킷의 용량과 milk1의 양
# 버킷1을 2에 붓고, 2를 3에 붓는 방식으로 100번 반복

def pour_milk(pour):
    pour_next = pour+1 # 다음에 부을 우유
    if pour_next == 4: # 1,2,3만 반복가능
        pour_next = 1
    sum_milk = milk[pour] + milk[pour_next] # 두 양동이를 합친 우유
    if sum_milk > bucket[pour_next]: # 양이 넘치는 경우
        milk[pour_next] = bucket[pour_next]
        milk[pour] = sum_milk - bucket[pour_next]
    else: # 양이 넘치지 않는 경우
        milk[pour_next] = sum_milk
        milk[pour] = 0


from sys import stdin

bucket = [0,] # 양동이 용량
milk = [0,] # 우유의 양
for i in range(3):
    b, m = map(int, stdin.readline().split())
    bucket.append(b)
    milk.append(m)
# print(bucket, milk)
# b = [0, 10, 11, 12]
# m = [0, 3, 4, 5]

cnt = 0
pour = 1 # 1,2,3 반복
while cnt < 100:
    pour_milk(pour)
    pour+=1
    cnt+=1
    if pour == 4:
        pour = 1

print(milk[1])
print(milk[2])
print(milk[3])

