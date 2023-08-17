def solution(cards):
    v = [0 for _ in range(len(cards)+1)]
    ans = []
    v[0] = 0
    for i in range(len(cards)):
        p = cards[i]
        cnt = 0
        while True:
            if v[p] == 0:
                v[p] = 1
                p = cards[p-1]
                cnt += 1
            else:
                break
        ans.append(cnt)
    ans.sort(reverse = True)
    return ans[0]*ans[1]