cnt = 0
def dfs(st,pron,past):
    global cnt
    if not st:
        cnt += 1
        return
    
    for i in pron:
        if i!=past and len(st)>=len(i) and st[:len(i)] == i:
            dfs(st[len(i):],pron,i)

def solution(babbling):
    pron = ["aya","ye","woo","ma"]
    for st in babbling:
        for i in pron:
            if st[:len(i)] == i:
                dfs(st[len(i):],pron,i)
    return cnt