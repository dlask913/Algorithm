def solution(s):
    answer = []
    dic={}
    for k,v in enumerate(s):
        if v not in dic:
            answer.append(-1)
        else:
            answer.append(k-dic[v])
        dic[v] = k
    return answer