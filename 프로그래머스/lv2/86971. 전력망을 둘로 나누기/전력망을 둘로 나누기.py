from collections import deque
def share_wire(dic, x, y):
    v = [0 for _ in range(len(dic))]
    v[x - 1] = 1
    q = deque([])
    for i in dic[x]:
        if i != y: q.append(i)
    cnt = 1
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if v[node-1] == 0:
                v[node-1] = 1
                cnt += 1
            for i in dic[node]:
                if v[i - 1] == 0:
                    q.append(i)
    return cnt


def solution(n, wires):
    answer = n
    dic = {i + 1: [] for i in range(n)}

    for i in wires:
        dic[i[0]].append(i[1])
        dic[i[1]].append(i[0])

    for i in wires:
        a = share_wire(dic, i[0], i[1])
        b = share_wire(dic, i[1], i[0])
        answer = min(abs(a - b),answer)
    return answer