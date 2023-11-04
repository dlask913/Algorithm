def conversion(num,x): # 10->N진수 변환 (숫자, 진법)
    dic = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    res = ''
    while num > 0:
        if num%x in dic: # 10~15 인 경우
            res += dic[num%x]
        else:
            res += str(num%x)
        num = num // x
    return res[::-1]

def solution(n, t, m, p): # 진법, 숫자 갯수, 게임 인원, 튜브 순서
    answer = ''
    tmp = '0' # 시작은 무조건 0
    for i in range(1,m*t):
        tmp += conversion(i,n)

    for i in range(t):
        answer += tmp[p-1]
        p += m
    
    return answer