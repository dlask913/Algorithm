zero,one = 0,0
def divide(arr,lx,rx,ly,ry):
    global zero,one
    if check(arr,lx,rx,ly,ry):
        if arr[lx][ly] == 1:
            one += 1
        else:
            zero += 1
        return
    
    kx = (lx+rx)//2 # x 중간
    ky = (ly+ry)//2 # y 중간
    divide(arr,lx,kx,ly,ky) # 위에서 오른쪽
    divide(arr,lx,kx,ky,ry) # 위에서 왼쪽
    divide(arr,kx,rx,ly,ky) # 아래에서 오른쪽
    divide(arr,kx,rx,ky,ry) # 아래에서 왼쪽

def check(arr,lx,rx,ly,ry): # 압축이 가능한지 확인
    flag = arr[lx][ly]
    for i in range(lx,rx):
        for j in range(ly,ry):
            if arr[i][j] != flag:
                return False
    return True
    
def solution(arr):
    divide(arr,0,len(arr),0,len(arr))
    return [zero,one]