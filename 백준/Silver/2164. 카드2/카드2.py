import sys
from collections import deque

n = int(sys.stdin.readline())
lst = deque()

for i in range(1,n+1):
    lst.append(i)

while len(lst)!=1:
    lst.popleft()
    lst.append(lst.popleft())
print(lst[0])