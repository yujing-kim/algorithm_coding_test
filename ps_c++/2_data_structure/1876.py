# 1876 스택수열


def main():
    stack = list()  # 넣을 스택
    want_li = list()  # 만들고 싶은 수열

    # 입력 받기
    num = int(input())  # 입력받음 # 수열 갯수
    for i in range(num):
        a = int(input())
        want_li.append(a)
    # print('want_li:' ,want_li)


    # solve
    tar = 0 # want_li의 인덱스
    answer_list = list() # 과정 배열
    for i in range(1,num+1):
        stack.append(i)
        answer_list.append('+')
        ## 스택 검사하기
        while True:
            if len(stack) <= 0: # 스택이 비어있으면 반환
                break
            if stack[-1] == want_li[tar]: # 타겟과 끝 원소가 같으면 pop
                # print('while:',i)
                stack.pop()
                answer_list.append('-')
                tar=tar+1 # 다음꺼 검사
            else :
                break


    # 답을 출력
    if len(stack) > 0 : # stack에 원소가 남아있으면 불가
        print('NO')
    else: # 원소가 0개이면 과정을 출력
        print('\n'.join(answer_list))

if __name__ == '__main__':
    main()