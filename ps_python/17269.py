# 17269 이름궁합
def start():
    global N,M,a,b
    global name_list
    name_list = list() # 이름을 한글자씩 번갈아서 넣음
    N,M = map(int,input().split())
    a,b = map(list,input().split())

    for i in range(min(N,M)):
        name_list.append(a.pop(0))
        name_list.append(b.pop(0))
    if len(a) > 0:
        name_list = name_list+a
    if len(b) > 0:
        name_list = name_list+b
    name_list = list(map(ord,name_list)) # 아스키코드 변환하여 넣기 # ord('A')
    name_list = [(i-65) for i in name_list] # 65('A') 빼기

    return

start() # 입력 + 배열처리

alph = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]

l = len(name_list)

name_list = [alph[i] for i in name_list]

while l > 2:
    new_list = list()
    for i in range(l-1):
        sum = (name_list[i]+name_list[i+1]) % 10
        new_list.append(sum)
    l = len(new_list)

    name_list = new_list
    # print(name_num_list)

print(str(name_list[0]*10 + name_list[1])+"%\n") # 답 출력



