import sys

n=int(sys.stdin.readline())
queue = []

for i in range(n):
    st = sys.stdin.readline().split()
    if st[0]=="push":
        queue.append(int(st[1]))
    if st[0]=="pop":
        if not queue:
            print(-1)
        else:
            print(queue.pop(0))
    if st[0] == "size":
        print(len(queue))
    if st[0] == "empty":
        if not queue:
            print(1)
        else:
            print(0)
    if st[0] == "back":
        if not queue:
            print(-1)
        else:
            print(queue[-1])
    if st[0] == "front":
        if not queue:
            print(-1)
        else:
            print(queue[0])