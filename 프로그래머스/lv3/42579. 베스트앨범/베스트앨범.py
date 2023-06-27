def solution(genres, plays):
    answer = []
    s = {genres[i]:0 for i in range(len(genres))}
    p = {genres[i]:[] for i in range(len(genres))}
    for k,v in enumerate(plays):
        s[genres[k]] += v
        p[genres[k]].append([k,v])
    
    s = sorted(s, key=lambda x:s[x],reverse=True)
    for i in s:
        p[i].sort(key=lambda x:-x[1])
        if len(p[i])>1:
            answer += [p[i][0][0],p[i][1][0]]
        else:
            answer += [p[i][0][0]]
            
    return answer