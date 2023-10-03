def solution(d, budget):
    ans = 0
    d.sort()
    for x in d:
        budget -= x
        if budget >= 0:
            ans += 1
        else:
            break
    return ans