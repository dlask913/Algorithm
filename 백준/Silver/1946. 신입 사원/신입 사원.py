import sys
t= int(sys.stdin.readline())
for _ in range(t):
    score = []
    n= int(sys.stdin.readline())
    cnt = 0
    for _ in range(n):
        a,b=map(int,sys.stdin.readline().split())
        score.append([a,b])
    score.sort()
    temp = score[0][1]
    for i in range(1,n):
        if temp > score[i][1]:
            cnt +=1
            temp=score[i][1]
    print(cnt+1)
