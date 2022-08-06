import heapq
import sys
n = int(sys.stdin.readline())
positive=[]
negative=[]

for i in range(n):
    x = int(sys.stdin.readline())
    if x==0:
        if not positive and not negative:
            print(0)
        elif positive and not negative: print(heapq.heappop(positive))
        elif negative and not positive: print(-heapq.heappop(negative))
        else:
            if positive[0] >= abs(negative[0]): print(-heapq.heappop(negative))
            else: print(heapq.heappop(positive))
    elif x>0:
        heapq.heappush(positive,x)
    else:
        heapq.heappush(negative,-x)
