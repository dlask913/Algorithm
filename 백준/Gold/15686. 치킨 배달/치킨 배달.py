import math,copy

n,m = map(int,input().split())
city = []
q=[]
result = []

for _ in range(n):
    city.append(list(map(int, input().split())))

def brute_force(x,cnt):
    if cnt >= m:
        q_temp = copy.deepcopy(q)
        d_cost(q_temp)
        return
    for i in range(x,n):
        for j in range(n):
            if city[i][j] == 2:
                city[i][j] = 0
                q.append((i, j))
                brute_force(i,cnt+1)
                q.pop()
                city[i][j] = 2

def d_cost(q_temp):

    cost = [[math.inf for _ in range(n)] for _ in range(n)]
    while q_temp:
        x,y=q_temp.pop(0)
        for i in range(n):
            for j in range(n):
                if city[i][j] == 1:
                    r = abs(x-i) + abs(y-j)
                    cost[i][j] = r if cost[i][j] > r else cost[i][j]
    sum_ = 0
    for i in cost:
        for j in i:
            if j < math.inf:
                sum_ += j
    result.append(sum_)

brute_force(0,0)

print(min(result))
