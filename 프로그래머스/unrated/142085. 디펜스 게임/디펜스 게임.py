import heapq
def solution(n, k, enemy):
    hq = []
    s = 0
    cnt = k
    for x in enemy:
        heapq.heappush(hq,-x)
        s += x
        if s>n and cnt>0:
            cnt -= 1
            s += heapq.heappop(hq)
        elif s>n and cnt==0:
            heapq.heappop(hq)
            break

    return len(hq)+(k-cnt)