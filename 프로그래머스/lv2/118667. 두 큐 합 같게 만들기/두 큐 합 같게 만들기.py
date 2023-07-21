from collections import deque
def solution(queue1, queue2):
    answer = -2
    s1,s2 = sum(queue1),sum(queue2)
    if (s1+s2)%2!=0: return -1
    q1,q2 = deque(queue1),deque(queue2)
    cnt = 0
    while True:
        if cnt>(len(q1)+len(q2)+2):
            return -1
        if s1 == s2:
            break
        if s1>s2:
            s1 -= q1[0]
            s2 += q1[0]
            q2.append(q1.popleft())
        elif s2>s1:
            s2 -= q2[0]
            s1 += q2[0]
            q1.append(q2.popleft())
        cnt += 1
    
    return cnt