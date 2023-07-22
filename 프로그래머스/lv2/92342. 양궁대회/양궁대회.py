import copy
res = [0,0]
ans = [0 for _ in range(11)]
def calculate(apeach,v):
    s = 0
    s2 = 0
    for key,val in enumerate(apeach):
        if v[key] == 0 and val>0:
            s  += key
        if v[key] == 1:
            s2 += key
    return s2-s
            
def brute_force(lion,apeach, score, v, arrow):
    global res, ans
    if arrow >= 0:
        tmp = calculate(apeach,v) # 어피치 점수
        if tmp > res[0]:
            res= [tmp,score]
            ans = copy.deepcopy(v)
            
    for i in range(1,11):
        if v[i] == 0 and arrow >= lion[i]:
            v[i] = 1
            score += i
            brute_force(lion, apeach, score, v, arrow - lion[i])
            score -= i
            v[i] = 0

def solution(n, info):
    answer = []
    info = info[::-1]
    lion = [0 for _ in range(11)]
    for key,val in enumerate(info):
        lion[key] = val + 1

    for i in range(10,0,-1):
        v = [0 for _ in range(11)]
        if n >= lion[i]:
            v[i] = 1
            brute_force(lion,info, i, v, n - lion[i])
    
    if res==[0,0]: return [-1]
    for i in range(11):
        if ans[i] != 0:
            ans[i] = lion[i]
            n -= lion[i]
    ans[0] = n if n>0 else 0
    
    return ans[::-1]