def solution(today, terms, privacies):
    answer = []
    y,m,d = today.split('.')
    t_total = (int(y)*12+int(m))*28+int(d)
    dic = {}
    for i in terms:
        x,y=i.split()
        dic[x] = int(y)
        
    for j,i in enumerate(privacies):
        ymd,t = i.split()
        y,m,d = ymd.split('.')
        y,m,d = int(y),int(m),int(d)
        dd = (m*28 + d) + int(dic[t])*28 - 1
        if dd >= (28*12):
            y += 1
            dd -= (28*12)
        y,m,d = y,dd//28,dd%28
        total = (y*12+m)*28 + d
        if total < t_total:
            answer.append(j+1)
        
    return answer