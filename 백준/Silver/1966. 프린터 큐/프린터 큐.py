from collections import deque
import sys

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split())))
    cnt = 0
    while q:
        temp = max(q)
        front = q.popleft() 
        m -= 1
        if temp == front:
            cnt += 1 
            if m < 0:
                print(cnt,end=' ')
                break
        else:   
            q.append(front) 
            if m < 0 :
                m = len(q) - 1
