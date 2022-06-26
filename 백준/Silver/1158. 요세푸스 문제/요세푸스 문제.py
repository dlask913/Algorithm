n,k = map(int,input().split())
lst = [(i+1) for i in range(n)]
que=[]
cnt = 1
i = 0
while lst:
    if i >= len(lst):
        i = 0
    if cnt == k:
        cnt = 0
        que.append(lst.pop(i))
    else:
        i += 1
    cnt += 1

print("<",end='')
for i in range(len(que)-1):
    print(que[i],end=', ')
print(que[-1],end='>')