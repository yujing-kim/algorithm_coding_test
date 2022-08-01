def solution(s):
    answer = 10000
    
    if len(s) == 1: return 1  # 문자열 길이 1
    
    for i in range(1,len(s)//2+1): 
        # i 단위로 자르기
        string, pre = '', 1
        result = [s[st:st+i] for st in range(0,len(s),i)]

        for idx,res in enumerate(result[1:],1):
            if result[idx-1] != res: # 앞에 것과 다르면
                if pre == 1: string +=result[idx-1]
                else: string += str(pre)+result[idx-1]
                pre=1
                if idx == len(result)-1: string+=res # 마지막 원소
            else: # 앞에것과 같으면
                pre+=1
                if idx == len(result)-1: string+= str(pre)+res # 마지막 원소
         
        if answer > len(string):
            answer = len(string)

    return answer