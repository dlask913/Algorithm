from collections import deque,Counter
def solution(weights):
    answer = 0
    weights.sort()
    for v in Counter(weights).values():
        if v>=2:
            answer += sum([i for i in range(1,v)])
    
    dq = deque(weights)
    tmp = []
    for _ in range(len(weights)-1):
        x = dq.popleft()
        tmp.append(x*2)
        tmp.append(x*3/2)
        tmp.append(x*4/3)
        
    c = Counter(tmp)
    for i in weights:
        answer += c[i]
    return answer