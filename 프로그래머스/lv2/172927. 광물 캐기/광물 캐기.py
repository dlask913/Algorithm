def solution(picks, minerals):
    answer = 0
    dic = {"diamond":[1,5,25],"iron":[1,1,5],"stone":[1,1,1]}
    l = len(minerals) if len(minerals) < sum(picks)*5 else sum(picks)*5
    m = [ minerals[i:i+5] for i in range(0, l, 5) ]
    v = []
    for i in range(len(m)):
        tmp = 0
        for j in m[i]:
            tmp += dic[j][2]
        v.append((i,tmp))
    v.sort(key=lambda x:-x[1])
    
    for i in v:
        k = 0
        for key,value in enumerate(picks):
            if value > 0:
                k = key
                picks[k]-=1
                break
        for j in m[i[0]]:
            answer += dic[j][k]
    
    return answer