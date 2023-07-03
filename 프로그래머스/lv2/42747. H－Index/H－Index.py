def solution(c):
    c.sort()
    ans = []
    v = 1
    for _ in range(len(c)):
        cnt = 0
        for i in range(len(c)):
            if v<=c[i]:
                cnt += 1
        if v<=cnt: ans.append(v)
        else: break
        v += 1
    if not ans: return 0
    return max(ans)