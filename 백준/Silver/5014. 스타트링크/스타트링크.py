from collections import deque
f,s,g,u,d = map(int,input().split())
v = [0 for _ in range(f+1)]

def startLink(x,y):
    q = deque()
    q.append((x,y))
    while q:
        cur, cnt = q.popleft()
        if cur == g:
            print(cnt)
            break

        for i in [(cur+u),(cur-d)]:
            if 0<i<=f and v[i] == 0:
                v[i] = 1
                q.append((i,cnt+1))

v[s] = 1
startLink(s,0)
if v[g] == 0: print("use the stairs")
