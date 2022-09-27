n,m=map(int,input().split())
tree = list(map(int,input().split()))
tree.sort()
start=1
end=tree[-1]

def binary_search(start,end):
    k = (start+end) //2
    if start > end:
        print(k)
        return
    branch = 0
    for i in tree:
        if i>k:
            branch += (i-k)

    if branch<m:
        binary_search(start,k-1)
    else:
        binary_search(k+1,end)

binary_search(start,end)
