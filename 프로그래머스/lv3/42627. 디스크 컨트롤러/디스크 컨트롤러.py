import heapq
def solution(jobs):
    answer = 0
    l = len(jobs)
    if l == 1: return jobs[0][1]-jobs[0][0]
    jobs.sort(key=lambda x:(x[0],x[1]))
    hq = [[jobs[0][1]]+jobs.pop(0)]
    cur = 0
    while hq:
        c,x,y = heapq.heappop(hq)
        if cur<x: cur = x
        cur += y
        answer += (cur-x)
        while jobs:
            if jobs[0][0]<=cur:
                heapq.heappush(hq,[jobs[0][1]]+jobs.pop(0))
            else:
                break
        if not hq and jobs:
            heapq.heappush(hq,[jobs[0][1]]+jobs.pop(0))
    
    return answer//l