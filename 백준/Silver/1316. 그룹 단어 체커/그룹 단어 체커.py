n= int(input())
cnt = 0
for i in range(n):
    st = input()
    flag = 1
    for j in range(len(st)-1):
        if st[j] != st[j+1]:
            temp = st[j+1:]
            if temp.count(st[j])>0:
                flag = 0
    if flag:
        cnt +=1
print(cnt)