""" DFS """
n,m = map(int,input().split())
t = input()
v = [0 for _ in range(n+1)] # 진실 + 겹치는 사람 처리
ans = 0
if t == "0": # 진실을 아는 사람이 0일 때
    ans = m
else:
    tmp = list(map(int,t.split()))
    for i in range(1,tmp[0]+1):
        v[tmp[i]] = 1

parties = []
for _ in range(m):
    parties.append(list(map(int,input().split())))

def dfs(s,v):
    for x in parties:
        if s in x[1:]:
            for i in range(1,x[0]+1):
                if v[x[i]] == 0:
                    v[x[i]] = 1
                    dfs(x[i],v)

for i in range(1,n+1):
    if v[i] == 1:
        dfs(i,v)

for party in parties:
    if ans == m: # 진실을 아는 사람이 0일 때
        break
    flag = True
    for x in party[1:]:
        if v[x] == 1:
            flag = False
    if flag:
        ans += 1

print(ans)