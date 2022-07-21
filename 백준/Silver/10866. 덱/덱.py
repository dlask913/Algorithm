import sys

n=int(sys.stdin.readline())
deque=[]
for i in range(n):
    st = sys.stdin.readline().split()
    if st[0]=="push_front":
        deque.insert(0,st[1])
    if st[0]=="push_back":
        deque.append(st[1])
    if st[0]=="pop_front":
        if deque:
            print(deque.pop(0))
        else:
            print(-1)
    if st[0]=="pop_back":
        if deque:
            print(deque.pop())
        else:
            print(-1)
    if st[0]=="size":
        print(len(deque))
    if st[0]=="empty":
        if deque:
            print(0)
        else:
            print(1)
    if st[0]=="front":
        if deque:
            print(deque[0])
        else:
            print(-1)
    if st[0]=="back":
        if deque:
            print(deque[-1])
        else:
            print(-1)
