import sys
n = int(sys.stdin.readline())
tree = list(map(int,sys.stdin.readline().split()))
node = int(sys.stdin.readline())

def dfs(v,tree):
    tree[v]=-2
    for i in range(len(tree)):
        if tree[i]==v:
            dfs(i,tree)

dfs(node,tree)

cnt = 0
for i in range(n):
    if tree[i]!=-2 and i not in tree:
        cnt += 1
print(cnt)
