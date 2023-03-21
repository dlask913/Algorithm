from collections import deque

n,m = map(int,input().split())
lst = list(map(int,input().split()))
dq = deque([i for i in range(1,n+1)])

cnt = 0
for i in lst:
    while True:
        if dq[0] == i:
            dq.popleft()
            break

        if dq.index(i) < len(dq)/2:
            while dq[0] != i:
                dq.append(dq.popleft())
                cnt += 1
        else:
            while dq[0] != i:
                dq.appendleft(dq.pop())
                cnt += 1
print(cnt)
