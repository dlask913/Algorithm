k = int(input())
tree= list(map(int,input().split()))
sol= [[] for _ in range(k)]

def dnq(tree,left,right,s,level):
    if left>= right:
        s[level].append(tree[left])
        return
    k = (right+left)//2
    s[level].append(tree[k])
    dnq(tree,left,k-1,s,level+1)
    dnq(tree,k+1,right,s,level+1)

dnq(tree,0,2**k-2,sol,0)

for i in sol:
    for j in i:
        print(j,end=' ')
    print()