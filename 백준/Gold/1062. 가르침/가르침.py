n,k = map(int,input().split())
check = 0
word = [0 for _ in range(n)]
ans = 0
def dfs(s,cnt,check):
    global ans
    if cnt == (k-5):
        tmp = 0
        for w in word:
            if (w & check) == w:
                tmp += 1
        ans = max(tmp,ans)
        return
    for i in range(s,26):
        if not (check & (1 << i)):
            check |= 1 << i
            dfs(i+1,cnt+1,check)
            check &= ~(1 << i)

for i in range(n):
    tmp = input()
    for x in tmp[4:-4]:
        word[i] |= 1 << (ord(x)-ord('a'))

check |= 1 << (ord('a')-ord('a'))
check |= 1 << (ord('n')-ord('a'))
check |= 1 << (ord('t')-ord('a'))
check |= 1 << (ord('i')-ord('a'))
check |= 1 << (ord('c')-ord('a'))

if k < 5:
    print(0)
else:
    dfs(1,0,check)
    print(ans)