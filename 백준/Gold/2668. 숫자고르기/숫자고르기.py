from collections import Counter
n = int(input())
dic = {}
v = [0 for _ in range(n+1)]
for i in range(1,n+1):
    x = int(input())
    dic[i] = x

res = []
def dfs(s,tmp):
    global res
    if len(tmp)>=2:
        c = Counter(tmp)
        for i in c:
            if c[i]%2==0:
                res.append(i)

    if v[dic[s]] < 2:
        v[dic[s]] += 1
        dfs(dic[s],tmp+[dic[s]])

for i in range(1,n+1):
    dfs(i,[i])

res = sorted(Counter(res),key=lambda x:x)
print(len(res))
for i in res:
    print(i)