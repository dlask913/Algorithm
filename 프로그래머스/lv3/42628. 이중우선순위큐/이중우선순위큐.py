import heapq
def solution(operations):
    hq = []
    max_hq = []
    
    for i in operations:
        x,y = i.split()
        if x=='I':
            heapq.heappush(hq,int(y))
            heapq.heappush(max_hq,-1*int(y))
        if x=='D' and y=='1':
            if not max_hq: continue
            heapq.heappop(max_hq)
            hq = [-1*i for i in max_hq]
            heapq.heapify(hq)
        if x=='D' and y=='-1':
            if not hq: continue
            heapq.heappop(hq)
            max_hq = [-1*i for i in hq]
            heapq.heapify(max_hq)
            
    if not hq: return [0,0]
    return [-max_hq[0],hq[0]]