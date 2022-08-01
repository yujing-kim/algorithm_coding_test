# 정렬 > 가장큰수
def solution(numbers):
    
    answer = ''
    numbers = list(map(str, numbers)) # 문자열로 바꾸기
    
    # 한자리씩 비교
    numbers.sort(key = lambda a : (a[0],a[1%len(a)],a[2%len(a)],a[3%len(a)]),reverse = True)
    
    answer = ''.join(numbers)
    
    return answer if int(answer) != 0 else '0'