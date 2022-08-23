import sys
n,m = map(int,sys.stdin.readline().split())
lst_n = set()
lst_m = set()

for _ in range(n):
    lst_n.add(sys.stdin.readline())
for _ in range(m):
    lst_m.add(sys.stdin.readline())

sol = sorted(list(lst_n & lst_m))

print(len(sol))
for i in sol:
    print(i.strip())
