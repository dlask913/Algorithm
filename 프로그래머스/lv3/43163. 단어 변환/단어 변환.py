
def checkWord(x,y):
    cnt = 0
    for i in range(len(x)):
        if x[i] != y[i]: cnt += 1
    if cnt==1: return True
    else: return False
    
def bfs(b,t,w):
    q = [b]
    v = [0 for _ in range(len(w))]
    cnt = 0
    while q:
        l = len(q)
        for _ in range(l):
            x = q.pop()
            if x==t: 
                break
            for i in range(len(w)):
                if checkWord(x,w[i]) and v[i]==0:
                    v[i] = 1
                    q.append(w[i])
        cnt += 1
    return cnt-1
    
    
        
def solution(begin, target, words):
    if target not in words:
        return 0
    if begin in words:
        words.remove(begin)
    return bfs(begin,target,words)
