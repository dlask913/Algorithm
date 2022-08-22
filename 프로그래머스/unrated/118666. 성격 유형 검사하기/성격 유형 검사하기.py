from collections import defaultdict
def solution(survey, choices):
    dic = defaultdict(int)
    answer=''
    for i,j in zip(choices,survey):
        if i > 4:
            dic[j[1]]+=(i-4)
        else:
            dic[j[0]]+=abs(i-4)
    
    if dic['R']>=dic['T']: answer+='R'
    else:                  answer+='T'
    
    if dic['C']>=dic['F']: answer+='C' 
    else:                  answer+='F'
    
    if dic['J']>=dic['M']: answer+='J'
    else:                  answer+='M'
    
    if dic['A']>=dic['N']: answer+='A'
    else:                  answer+='N' 

    return answer