n = int(input())
cnt = 0
for i in range(1,n+1):
    temp = list(str(i))
    li = list(map(int,temp))
    if len(li)==1:
        cnt += 1
        continue
    m = (li[0]-li[1])
    flag = 1
    for j in range(1,len(li)):
        if (li[j-1]-li[j])!=m:
            flag = 0
            break
    if flag:        
        cnt +=1
print(cnt)

