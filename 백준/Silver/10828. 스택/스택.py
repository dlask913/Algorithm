import sys

n=int(sys.stdin.readline())
stack = []
for i in range(n):
    st = sys.stdin.readline().split()
    if st[0]=="push":
        stack.append(int(st[1]))
    if st[0]=="pop":
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    if st[0] == "size":
        print(len(stack))
    if st[0] == "empty":
        if not stack:
            print(1)
        else:
            print(0)
    if st[0] == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])
