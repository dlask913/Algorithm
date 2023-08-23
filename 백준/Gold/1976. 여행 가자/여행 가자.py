from collections import deque
n = int(input())
m = int(input())
g = []
v = [0 for _ in range(n)]
for i in range(n):
    g.append(list(map(int,input().split())))
res = list(map(int,input().split()))
ans = ''
q = deque([res[0]-1])
while q:
    for _ in range(len(q)):
        x = q.popleft()
        v[x] = 1
        for key,val in enumerate(g[x]):
            if val == 1 and v[key] == 0:
                q.append(key)
flag = True
for i in res:
    if v[i-1] == 0:
        print("NO")
        flag = False
        break
if flag:
    print("YES")