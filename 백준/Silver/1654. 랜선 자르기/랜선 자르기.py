k,n = map(int,input().split())
line = []
for _ in range(k):
    line.append(int(input()))

start = 1
end= sum(line)//n
d = []
while start<=end:
    k = (start+end)//2
    cnt = 0
    for i in line:
        cnt += i//k
    if cnt >=n:
        start = k+1
        d.append(k)
    else:
        end = k-1
print(max(d))

