n= int(input())
lst = []
visited = [0 for _ in range(n)]
for _ in range(n):
    lst.append(list(map(int,input().split())))

def search(start,lst,v):
    for i in range(n):
        if lst[start][i]==1 and v[i]==0:
            v[i]=1
            search(i,lst,v)

for i in range(n):
    v=[0 for _ in range(n)]
    search(i,lst,v)
    visited[i]=v

for i in visited:
    for j in i:
        print(j,end=' ')
    print()