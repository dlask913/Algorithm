N = int(input())
video = []
for _ in range(N):
    video.append(list(input()))

def quad_tree(l,r,n):
    check = video[l][r]
    flag = True
    for i in range(l,l+n):
        for j in range(r,r+n):
            if video[i][j] != check:
                flag = False
    if flag:
        print(check,end='')
        return
    print('(',end='')
    n=n//2
    quad_tree(l,r,n)
    quad_tree(l,r+n,n)
    quad_tree(l+n,r,n)
    quad_tree(l+n,r+n,n)
    print(')',end='')

quad_tree(0,0,N)
