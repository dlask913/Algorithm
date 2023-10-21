from collections import deque
n, k = map(int,input().split())

def bfs(m):
    v = [0 for _ in range(100001)]
    q = deque()
    q.append((m,0))
    while q:
        x,t = q.popleft()
        if x == k:
            return t

        v[x] = 1 # 방문 처리
        for i in (x*2,x-1,x+1): # x*2 를 먼저 해야함 ( 참고:https://www.acmicpc.net/board/view/38887#comment-69010 )
            if 0 <= i <= 100000 and v[i] == 0:
                if i == x*2: # 순간 이동
                    q.append((i,t))
                else:
                    q.append((i,t+1))

res = bfs(n)
print(res)