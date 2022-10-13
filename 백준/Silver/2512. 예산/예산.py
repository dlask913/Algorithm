n=int(input())
cost=list(map(int,input().split()))
m = int(input())
result=[]
start = 0
end = max(cost)

while start<=end:
    k= (start+end)//2
    s=0
    for i in cost:
        if i>=k:
            s+=k
        else:
            s+=i
    if s>m:
        end=k-1
    else:
        start=k+1
        result.append(k)

print(max(result))