import sys
m,n = map(int,sys.stdin.readline().split())
for i in range(m,n+1):
    if i >1:
        flag = 1
        for j in range(2,int(i**(1/2))+1):
            if i%j==0:
                flag = 0
                break
        if flag:
            print(i)