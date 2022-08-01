# 5543 상근날드
burger_list = list()
answer = 0
def innum():
    for i in range(5):
        a = int(input())
        burger_list.append(a)

def solve():
    burger_min = min(burger_list[:3])
    bever_min = min(burger_list[-2:])

    # print(burger_min, bever_min)
    answer = burger_min + bever_min

    print(answer-50)

def main():
    innum() # 입력받기
    # print(burger_list)
    solve()
    pass

if __name__ == '__main__':
    main()