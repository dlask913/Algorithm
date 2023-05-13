from collections import deque
def solution(keymap, targets):
    answer = []
    for t in targets:
        q = deque(list(t))
        res = 0
        flag = False
        while q:
            s = q.popleft()
            m = 100
            for k in keymap:
                if s in k:
                    m = min(m,(k.index(s)+1))
            res += m
            if m==100:
                flag = True
        if flag: answer.append(-1)
        else:   answer.append(res)
    return answer