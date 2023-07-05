def solution(name):
    answer = 0
    if all(x == 'A' for x in name):
        return 0
    c = [0 for _ in range(len(name))]
    for i in range(len(name)):
        c[i] = min(ord(name[i])-65,abs(ord(name[i])-65-26))
    
    idx, cnt = 0, 0
    sol = []
    flag = False
    for k in range(len(c)):
        if k!=0 and name[k] == 'A':
            if all(x == 'A' for x in name[k:]):
                sol.append(k-1)
            if cnt == 0: 
                idx = k
            cnt += 1
            flag = True
        if name[k] != 'A' and flag:
            sol.append(min(((idx-1) * 2 + (len(name) - (idx + cnt))), (len(name) - (idx + cnt)) * 2 + (idx-1)))
            cnt = 0
            flag = False
    sol.append(len(name)-1)
    if sol:    ans = (min(sol)+sum(c))
    else:      ans = sum(c)+len(name)-1
    return ans