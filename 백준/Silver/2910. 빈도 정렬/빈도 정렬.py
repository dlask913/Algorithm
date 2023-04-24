n, c = map(int, input().split())
lst = list(map(int, input().split()))
dic = {}

for i in lst:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

dic = sorted(dic.items(), key=lambda x:x[1],reverse=True)
for i,j in dic:
    print((str(i)+' ')*j,end='')
