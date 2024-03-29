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
        total = (int(y)*12+int(m))*28+int(d) + int(dic[t])*28 - 1
        if total < t_total:
            answer.append(j+1)
        
    return answer