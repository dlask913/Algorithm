from collections import deque
def solution(p, location):
    answer = 1
    pro = deque([(chr(i),p[i-65]) for i in range(ord('A'),ord('A')+len(p))])
    q = []
    while pro:
        q.append(pro.popleft())
        if q[-1][1] < max(p):
            pro.append(q.pop())
        else:
            p.remove(max(p))
    for i in q:
        if ord(i[0])-65 == location:
            break
        answer += 1    
    return answer