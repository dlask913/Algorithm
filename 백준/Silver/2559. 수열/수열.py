n,k=map(int,input().split())
lst = list(map(int,input().split()))
s =[]
res = []
temp = 0
for i in lst:
    temp += i
    s.append(temp)

p1,p2=0,k-1
while True:
    if p2>=n: break
    res.append(s[p2]-s[p1]+lst[p1])
    p1 += 1
    p2 += 1
print(max(res))
