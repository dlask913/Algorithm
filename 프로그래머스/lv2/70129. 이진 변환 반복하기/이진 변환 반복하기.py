def to_binary(c):
    b=[]
    while c!=0:
        b.append(c%2)
        c//=2
    b.reverse()
    b=list(map(str,b))
    return ''.join(b)
    
def solution(s):
    ans = [1,0]
    while True:
        ans[1] += s.count('0')
        s= ''.join(s.split('0'))
        c=int(len(s))
        if c==1: break
        s=to_binary(c)
        ans[0]+=1
    
    return ans