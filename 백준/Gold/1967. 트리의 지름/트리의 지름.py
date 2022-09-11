import sys
sys.setrecursionlimit(10000)
n = int(input())
tree=[[] for _ in range(10002)]
c=[]
def dfs(start,cost):
    if not tree[start]:
        c.append(cost)
    for i in tree[start]:
        dfs(i[0],cost+i[1])

for _ in range(n-1):
    x,y,z = map(int,input().split())
    tree[x].append([y,z])

max_=0
for i in range(1,n+1):
    temp=[]
    if tree[i]:
        for j in tree[i]:
            c=[]
            dfs(j[0],j[1])
            temp.append(max(c))
        if len(temp)>1:
            temp.sort()
            max_= temp[-1]+temp[-2] if max_<(temp[-1]+temp[-2]) else max_
        if len(temp)==1:
            temp.sort()
            max_= temp[-1] if max_ < temp[-1] else max_
print(max_)