def solution(k, tangerine):
    answer = 0
    dic = {}
    for x in tangerine:
        if x not in dic:
            dic[x]=1
        else:
            dic[x]+=1
    arr = sorted(dic.values(), key=lambda x: -x)
    
    for v in arr:
        if k<=0:
            break
        k -= v
        answer += 1
        
    return answer