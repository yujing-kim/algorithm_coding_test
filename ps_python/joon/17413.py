# 17413_단어뒤집기2
string = input()
answer, word, tag_flag = '','',0
# 답,   뒤집을단어, 태그

for s in string:
    if s == '<': # 태그의 시작인 경우
        tag_flag = 1
        answer+=word[::-1] # word를 뒤집어서 넣기
        word = ''

    if tag_flag == 1: # 태그인 경우
        answer+=s
    elif tag_flag == 0 and s == ' ': # 태그가 아니고 공백인 경우
        answer+=word[::-1]+s
        word=''
    else: # 태그가 아닌데 공백이 아닌경우
        word+=s

    if s == '>': # 태그의 마지막인 경우
        tag_flag = 0
        word = ''

print(answer+word[::-1])

