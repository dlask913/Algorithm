import sys
sys.setrecursionlimit(10 ** 9)
n = int(input())
tree= [[] for _ in range(n+1)]
parents=[0 for _ in range(n+1)]

for i in range(n-1):
    x,y= map(int,input().split())
    tree[x].append(y)
    tree[y].append(x)

def dfs(idx,tree,parents):
    for i in tree[idx]:
        if parents[i]==0:
            parents[i]=idx
            dfs(i,tree,parents)

dfs(1,tree,parents)

for i in range(2,n+1):
    print(parents[i])
