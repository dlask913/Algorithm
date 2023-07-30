def solution(routes):
    routes.sort(key=lambda x:(x[1],x[0]))
    camera = routes[0][1]
    cnt = 1
    for k, v in enumerate(routes[:-1]):
        flag = False
        if routes[k + 1][0] <= camera <= routes[k + 1][1]:
            flag = True
        if not flag:
            cnt += 1
            camera = routes[k + 1][1]
    return cnt