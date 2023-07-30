def solution(routes):
    routes.sort(key=lambda x:(x[1],x[0]))
    q = [routes[0][1]]
    cnt = 1
    for k, v in enumerate(routes[:-1]):
        l = len(q)
        for _ in range(l):
            i = q.pop()
            if routes[k + 1][0] <= i <= routes[k + 1][1]:
                q.append(i)
        if not q:
            cnt += 1
            q = [routes[k + 1][0], routes[k + 1][1]]
    return cnt