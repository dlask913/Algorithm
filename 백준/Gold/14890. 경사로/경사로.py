n,l = map(int,input().split())
lst =[]
cnt = 0
for _ in range(n):
    lst.append(list(map(int,input().split())))

def load(x,y,lev):
    global cnt
    if lev == 1: temp = lst[x]
    elif lev == 3: temp = [i[y] for i in lst]
    idx = 0
    flag = -1
    while idx < (n-1):
        cur = temp[idx]
        if cur - 1 == temp[idx + 1] and (idx+l) < n:
            if len(set(temp[idx+1:idx+l+1]))==1:
                flag = idx+l
                idx += l
            else:
                return
        elif cur + 1 == temp[idx+1] and idx>=l-1 and flag < idx-l+1:
            if len(set(temp[idx-l+1:idx+1]))==1:
                idx += 1
            else:
                return
        elif idx<(n-1) and temp[idx] == temp[idx+1]:
            idx += 1
        else:
            return
    cnt += 1

for i in range(n):
    for j in range(n):
        if i==0:
            load(i, j, 3)
        if j==0:
            load(i,j,1)

print(cnt)