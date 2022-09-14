import sys

n= int(sys.stdin.readline())
row = [0]* n
cnt = 0
def check(x):
    for i in range(x):
        if row[x]==row[i] or abs(row[x]-row[i])==abs(x-i):
            return False
    return True

def queens(x):
    global cnt
    if x==n:
        cnt += 1
        return
    else:
        for i in range(n):
            row[x]=i
            if check(x):
                queens(x+1)

queens(0)
print(cnt)