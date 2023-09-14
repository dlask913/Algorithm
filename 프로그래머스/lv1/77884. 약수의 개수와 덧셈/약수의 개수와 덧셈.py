def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        cnt = 0
        for j in range(1,int(i**0.5)+1):
            if i%j == 0:
                cnt += 2
            if j**2 == i:
                cnt -= 1
        if cnt%2==0:
            answer += i
        else:
            answer -= i
    return answer