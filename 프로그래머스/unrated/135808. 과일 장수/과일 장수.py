from collections import Counter
def solution(k, m, score):
    ans = 0
    score = sorted(Counter(score).items(), key=lambda x: -x[0]) 
    
    cnt = 0
    for i,j in score:
        cnt += j
        if cnt>=m:
            ans += (i*m*(cnt//m))
            cnt %= m
            
    return ans