def getSequence(k): # 1. 우박수열 만들기
    seqeunce = [k]
    while k > 1:
        if k%2 == 0:
            k//=2
        else:
            k = k*3 +1
        seqeunce.append(k)
    return seqeunce

def getArea(n,nums): # 2. 넓이 구하기
    area = []
    for i in range(1,n+1):
        area.append(min(nums[i-1],nums[i])+abs(nums[i]-nums[i-1])/2)
    return area

def fsum(x,y,num): # 3. 주어진 범위 총 넓이 계산
    s = 0.0
    for i in range(x,y):
        s += num[i]
    return s

def solution(k, ranges):
    answer = []
    seq = getSequence(k)
    
    n = len(seq)-1
    area = getArea(n,seq)

    for a,b in ranges:
        b = b if b>0 else b+n
        res = fsum(a,b,area) if a<=b else -1
        answer.append(res)
        
    return answer