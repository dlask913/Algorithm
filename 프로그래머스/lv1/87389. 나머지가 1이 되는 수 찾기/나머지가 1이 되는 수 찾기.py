def solution(n):
    answer = n
    for i in range(2,n):
        if n%i==1:
            answer=i
            break
    return answer