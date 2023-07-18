res = []
def dfs(start,tick,v,ans):
    global res
    x,y = tick[start]
    if all(v):
        res.append(ans)
    for key,val in enumerate(tick):
        if val[0] == y and v[key] == 0:
            v[key] = 1
            dfs(key,tick,v,ans+[val[1]])
            v[key] = 0

def solution(tickets):
    for key,val in enumerate(tickets):
        v = [0 for _ in range(len(tickets))]
        if val[0]=="ICN":
            v[key] = 1
            dfs(key,tickets,v,val)
    res.sort()        
    return res[0]