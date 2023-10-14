def solution(seq):
    ans = -100000
    n = len(seq)
    if n == 1: # 수열의 길이가 하나일 때
        return abs(seq[0])
    tmp = []
    tmp.append([-seq[x] if x%2==0 else seq[x] for x in range(n)]) # -1 로 시작하는 펄스 수열 곱
    tmp.append([-seq[x] if x%2!=0 else seq[x] for x in range(n)]) # 1 로 시작하는 펄스 수열 곱

    for arr in tmp:
        dp = [-100000 for _ in range(n)] # 최대값 갱신
        dp[0] = arr[0]
        for i in range(1,n): # 연속구간 최대 부분합 구하기  
            dp[i] = max(dp[i-1] + arr[i], arr[i])
        ans = ans if ans > max(dp) else max(dp)
    
    return ans