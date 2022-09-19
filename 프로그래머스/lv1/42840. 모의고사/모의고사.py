def solution(answers):
    a=[1,2,3,4,5]*2000
    b=[2,1,2,3,2,4,2,5]*1250
    c=[3,3,1,1,2,2,4,4,5,5]*1000
    cnt = [0,0,0]
    ans=[]
    idx=0
    for i in answers:
        cnt[0] = cnt[0]+1 if a[idx]==i else cnt[0]
        cnt[1] = cnt[1]+1 if b[idx]==i else cnt[1]
        cnt[2] = cnt[2]+1 if c[idx]==i else cnt[2]
        idx+=1
    
    for i in range(3):
        if cnt[i]==max(cnt): ans.append(i+1)
        
    return ans