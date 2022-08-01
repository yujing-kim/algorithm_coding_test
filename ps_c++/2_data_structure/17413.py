
#17413 단어 뒤집기2


st = str(input())
tag_flag = 0

word = str()
for i in st:
    if i == '<':
        tag_flag = 1
        new_word = word.split(' ')
        for idx, j in enumerate(new_word):
            if idx == len(new_word)-1:
                print(j[::-1], end='')
                word = ''
            else :
                print(j[::-1], end=' ')

    if tag_flag == 1:
        print(i, end='')

    else :
        word = word + i

    if i == '>':
        tag_flag = 0

if len(word) > 0: # 태그가 없는 문자열의 경우
    new_word = word.split(' ')
    for idx, j in enumerate(new_word):
        if idx == len(new_word) - 1:
            print(j[::-1], end='')
            word = ''
        else:
            print(j[::-1], end=' ')