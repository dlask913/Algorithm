from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque(truck_weights)
    cross_q = deque([])
    s = 0
    while q:
        x = q[0]
        if len(cross_q) >= bridge_length:
            s -= cross_q[0]
            cross_q.popleft()
        if (x + s) <= weight:
            cross_q.append(q.popleft())
            s += cross_q[-1]
        else:
            cross_q.append(0)
        answer += 1
    return answer + bridge_length