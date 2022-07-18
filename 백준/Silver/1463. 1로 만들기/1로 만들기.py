x = int(input())
sol = [0 for _ in range(10000000)]

for i in range(2,x+1):
    sol[i] = sol[i-1]+1
    if i % 2 == 0:  sol[i]=min(sol[i],sol[i//2]+1)
    if i % 3 == 0:  sol[i]=min(sol[i],sol[i//3]+1)

print(sol[x])