n = int(input())
team = list(map(int, input().split()))
dp = [0 for _ in range(n+1)]

for i in range(n+1):
    for j in range(i,0,-1):
        good = max(team[i-1],team[j-1]) # j~i 까지의 최댓값
        bad = min(team[i-1],team[j-1]) # j~i 까지의 최솟값
        dp[i] = max(dp[i], dp[j-1] + good - bad) # ★ 점화식

print(dp[n])