n,k=map(int,input().split())
st= list(input())
cnt = 0
for i in range(n):
    if st[i] =='P':
        for j in range(i-k,i+k+1):
            if j>=0 and j<n and st[j]=='H':
                cnt += 1
                st[j]='X'
                break
print(cnt)

