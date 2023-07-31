import heapq

n = int(input())
m = int(input())
dic = {i:[] for i in range(1,n+1)}
v = [0 for _ in range(n + 1)]
v[0]= 1
for _ in range(m):
    x,y,c = map(int,input().split())
    heapq.heappush(dic[x],(c,y))
    heapq.heappush(dic[y],(c,x))

q = [(0,1)]
ans = 0
while q:
    c,p = heapq.heappop(q)
    if v[p] == 0:
        v[p] = 1
        ans += c
        for i in dic[p]:
            heapq.heappush(q,i)
print(ans)