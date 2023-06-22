def solution(p, limit):
    ans = 0
    p.sort()
    l,r = 0,len(p)-1
    v=[0 for _ in range(r+1)]
    
    while l<r:
        if (p[l]+p[r])>limit:
            r-=1
        else:
            ans+=1
            v[l],v[r]=1,1
            l+=1
            r-=1
            
    for i in v:
        if i==0: ans+=1
    return ans