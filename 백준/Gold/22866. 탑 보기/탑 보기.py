
n = int(input())
h = list(map(int,input().split()))
inf = 1000001
dist = [inf for _ in range(n)]
cnt = [0 for _ in range(n)]
stack = []
# 왼 -> 오
for k in range(n):
    while stack and h[stack[-1]] <= h[k]:
        stack.pop()
    if stack and abs(dist[k]-k) > abs(k-stack[-1]):
        dist[k] = stack[-1]
    cnt[k] += len(stack)
    stack.append(k)

# 오 -> 왼
stack = []
for k in range(n-1,-1,-1):
    while stack and h[stack[-1]] <= h[k]:
        stack.pop()
    if stack and abs(dist[k]-k) > abs(k-stack[-1]):
        dist[k] = stack[-1]
    cnt[k] += len(stack)
    stack.append(k)

for i in range(n):
    if cnt[i] == 0:
        print(0)
    else:
        print(cnt[i], dist[i]+1)