res = 0
def dfs(s,cnt,num,t):
    global res
    if cnt>=len(num):
        if s == t: 
            res += 1
        return
    cnt += 1
    dfs(s+num[cnt-1],cnt,num,t)
    dfs(s-num[cnt-1],cnt,num,t)
    
def solution(numbers, target):
    dfs(0,0,numbers,target)
    return res