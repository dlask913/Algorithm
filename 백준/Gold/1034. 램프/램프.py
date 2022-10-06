n,m=map(int,input().split())
lst = []
lamp = []
for _ in range(n):
    lst.append(list(input()))
k=int(input())
max_ = 0

for i in range(n):
    lamp.append(lst[i].count('0'))

for i in range(n):
    if lamp[i]<=k and (k-lamp[i])%2==0:
        temp=lst[i]
        cnt = 0
        for j in range(n):
            if temp ==lst[j]:
                cnt += 1
        max_ = max_ if max_>cnt else cnt

print(max_)