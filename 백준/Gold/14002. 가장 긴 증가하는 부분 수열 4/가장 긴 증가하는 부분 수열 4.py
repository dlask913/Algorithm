n = int(input())
A = list(map(int, input().split()))
dp = [0 for _ in range(n + 1)]
res = []

for i in range(1, n):
    for j in range(i - 1, -1, -1):
        if A[i] > A[j]: # 현재 값(A[i]) 보다 작은 값들의 수 저장 
            dp[i] = max(dp[i], dp[j] + 1)

val = max(dp)
for i in range(n - 1, -1, -1): # 가장 큰 값~0 까지 수열 구하기
    if dp[i] == val:
        val -= 1
        res.append(A[i])

res.reverse()
print(max(dp)+1)
print(*res)
