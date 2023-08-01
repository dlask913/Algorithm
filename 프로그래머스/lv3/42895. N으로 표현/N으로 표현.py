def calculate(x,y):
    r = set([])
    for i in x:
        for j in y:
            r.add(i+j)
            r.add(i-j)
            r.add(i*j)
            if j!=0 and i%j==0: r.add(i//j)
    return r

def solution(N, number):
    answer = -1
    if N == number:
        return 1
    res = {1:[N]}
    for c in range(2,9):
        tmp = set([int(str(N)*c)])
        for i in range(1,c):
            tmp.update(calculate(res[i],res[c-i]))
        if number in tmp:
            return c
        res[c] = list(tmp)
    
    return answer