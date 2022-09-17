n,c = map(int,input().split())
x = []
d = []
for _ in range(n):
    x.append(int(input()))
x.sort()

start = 1
end = x[-1]-x[0]
d = []
while start<=end:
    cnt = 1
    k = (start+end)//2
    current = x[0]
    for i in x:
        if current+k <= i:
            cnt += 1
            current=i
    if cnt>=c:
        start = k+1
        d.append(k)
    else:
        end = k-1

print(max(d))