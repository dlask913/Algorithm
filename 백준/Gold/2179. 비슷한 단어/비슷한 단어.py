n = int(input())
word = []

for i in range(n):
    word.append(input())
w = sorted(list(enumerate(word)),key=lambda x:x[1])

m= 0
siz = [0 for _ in range(n)]
for i in range(1,n):
    cnt = 0
    if w[i-1][1][0] == w[i][1][0]:
        for j in range(min(len(w[i-1][1]),len(w[i][1]))):
            if w[i-1][1][j] == w[i][1][j]:
                cnt += 1
            else:
                break
    m = max(m, cnt)
    siz[w[i-1][0]] = max(siz[w[i-1][0]],cnt)
    siz[w[i][0]] = max(siz[w[i][0]],cnt)

flag = True
prefix = ''
m = max(siz)
for k,v in enumerate(siz):
    if v == m and flag:
        flag = False
        prefix = word[k][:m]
        print(word[k])
    elif v == m and not flag and prefix == word[k][:m]:
        print(word[k])
        break