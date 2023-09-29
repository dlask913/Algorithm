""" 비트마스킹 """
n,k = map(int,input().split())
check = 0 # 방문한 알파벳 비트 마스킹
word = [0 for _ in range(n)]
ans = 0
def dfs(s,cnt,check):
    global ans
    if cnt == (k-5): # antic 제외한 k 개만큼 알파벳 방문 했을 떄
        tmp = 0
        for w in word:
            if (w & check) == w: # 문자와 방문 가능한 알파벳 and 연산 했을 때, w와 같다면 방문 가능
                tmp += 1
        ans = max(tmp,ans)
        return
    for i in range(s,26):
        if not (check & (1 << i)): # 해당 알파벳을 방문하지 않았다면
            check |= 1 << i # 방문 처리
            dfs(i+1,cnt+1,check) # 탐색
            check &= ~(1 << i) # 탐색 후 새로운 조합을 위한 방문 처리 무효

for i in range(n):
    tmp = input()
    for x in tmp[4:-4]:
        word[i] |= 1 << (ord(x)-ord('a')) # antic 제외한 문자열 or 연산을 통한 비트 마스킹

# antic 방문 처리
check |= 1 << (ord('a')-ord('a'))
check |= 1 << (ord('n')-ord('a'))
check |= 1 << (ord('t')-ord('a'))
check |= 1 << (ord('i')-ord('a'))
check |= 1 << (ord('c')-ord('a'))

if k < 5: # 5개(antic) 미만인 경우 처리 불가
    print(0)
else:
    dfs(1,0,check)
    print(ans)
