res = 0
def bruteforce(s,dun,v,fat,c):
    global res
    if dun[s][0]<=fat:
        c+=1
        fat -= dun[s][1]
        res = res if res>c else c
    for i in range(len(dun)):
        if v[i] == 0 and dun[i][0]<=fat:
            v[i] = 1
            bruteforce(i,dun,v,fat,c)
            v[i] = 0

def solution(k, dun):
    v = [0 for _ in range(len(dun))]

    for i in range(len(dun)):
        tmp = k
        v[i] = 1
        bruteforce(i,dun,v,tmp,0)
        v[i] = 0
    
    return res