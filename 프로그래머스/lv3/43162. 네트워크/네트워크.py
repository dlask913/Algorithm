def dfs(start,v,com,n):
    v[start]=1
    for i in range(n):
        if com[start][i]==1 and v[i]==0:
            v[i]=1
            dfs(i,v,com,n)
    
def solution(n, com):
    answer = 0
    v = [0 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if com[i][j]==1 and v[i]==0:
                v[i]=1
                answer+=1
                dfs(j,v,com,n)
    return answer