# (x+1) * (y+1) * (z+1) -1
def solution(clothes):
    answer = 1
    dic = {}    
    for n,k in clothes:
        if k not in dic:
            dic[k]=1
        else:
            dic[k]+=1
    if len(dic)==1: return len(clothes)
    
    val = list(dic.values())
    for i in val:
        answer *= (i+1)
    
    return answer-1