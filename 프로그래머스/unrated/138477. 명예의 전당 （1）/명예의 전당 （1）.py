import heapq
def solution(k, score):
    answer = []
    hq = []
    
    for x in score:
        heapq.heappush(hq,x)
        if len(hq)>k:
            heapq.heappop(hq)
            
        tmp = heapq.heappop(hq)
        answer.append(tmp)
        heapq.heappush(hq,tmp)
    
    return answer