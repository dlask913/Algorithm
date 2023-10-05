n= int(input())
x,y = map(int,input().split())
l = int(input())
seq = []
ans = []
for _ in range(l):
    seq.append(int(input()))
    
def bruteforce(lev,cost,a,b):
    global ans
    if lev >= l:
        ans.append(cost)
        return
    bruteforce(lev+1, cost+abs(a-seq[lev]),seq[lev],b)
    bruteforce(lev+1, cost+abs(b-seq[lev]),a,seq[lev])
    
bruteforce(0,0,x,y)
print(min(ans))
