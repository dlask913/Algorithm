n = int(input())
w=[]
cost = []
visited = [0 for _ in range(n)]
for _ in range(n):
    w.append(list(map(int,input().split())))

def TSP(start,end,v,c):
    if 0 not in v:
        if w[start][end] != 0:
            cost.append(c+w[start][end])
    for i in range(n):
        if v[i]==0 and w[start][i] != 0:
            v[i]=1
            TSP(i,end,v,c+w[start][i])
            v[i]=0


for i in range(n):
    visited[i]=1
    TSP(i,i,visited,0)
    visited[i]=0

print(min(cost))
