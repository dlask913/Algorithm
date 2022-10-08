import heapq
v,e=map(int,input().split())
tree= {x:[] for x in range(v+1)}

for _ in range(e):
    a,b,c=list(map(int,input().split()))
    tree[a].append([c,b])
    tree[b].append([c,a])

def MST(start,cost):
    T=set([start])
    queue=tree[start]
    heapq.heapify(queue)
    while queue:
        c,n=heapq.heappop(queue)
        if n not in T:
            cost += c
            T.add(n)
            for i,j in tree[n]:
                if j not in T:
                    heapq.heappush(queue,[i,j])
    print(cost)

MST(1,0)