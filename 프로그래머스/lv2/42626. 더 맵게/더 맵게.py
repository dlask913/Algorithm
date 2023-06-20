import heapq
def solution(scoville, k):
    cnt = 0
    heapq.heapify(scoville)
    while True:
        if len(scoville)<2 and scoville[0]<k: return -1
        elif len(scoville) == 1 and scoville[0] >=k: break
        one = heapq.heappop(scoville)
        two = heapq.heappop(scoville)
        if one >= k:
            break
        heapq.heappush(scoville,one+two*2)
        cnt += 1
    return cnt