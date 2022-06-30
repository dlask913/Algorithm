import sys

n=int(sys.stdin.readline())
flag = 1
for i in range(n):
    stack = []
    st = input().strip()
    flag=1
    for j in range(len(st)):
        if st[j] == "(":
            stack.append(st[j])
        elif len(stack) != 0 and st[j] == ")":
            stack.pop()
        else:
            flag = 0
    if not stack and flag:
        print("YES")
    else:
        print("NO")


