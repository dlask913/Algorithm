import sys


front = list(sys.stdin.readline().strip())
back = []
n=int(sys.stdin.readline())
cursor = len(front)+1
for i in range(n):
    edi = sys.stdin.readline().split()
    if edi[0] == "L" and cursor > 1:
        back.append(front.pop())
        cursor -=1
    if edi[0] == "D" and back:
        front.append(back.pop())
        cursor +=1
    if edi[0] == "B" and cursor > 1:
        front.pop()
        cursor -=1
    if edi[0] =="P":
        front.append(edi[1])
        cursor +=1
back.reverse()
front += back
print(''.join(front))
