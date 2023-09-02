from collections import Counter
def solution(X, Y):
    inter = set(X)&set(Y)
    if not inter:
        return "-1"
    x = Counter(X)
    y = Counter(Y)
    
    answer = []
    for i in inter:
        answer += [i]*min(x[i],y[i])
    res = ''.join(sorted(answer)[::-1])
    
    if all(i == "0" for i in res):
        return "0"
    
    return res