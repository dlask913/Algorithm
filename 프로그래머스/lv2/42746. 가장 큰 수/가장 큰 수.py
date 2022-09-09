def solution(numbers):
    n=sorted(list(map(str,numbers)),key=lambda x:((x*4)[0:]),reverse=True)
    if all(i=='0' for i in n):
        answer='0'
    else:
        answer=''.join(n)
    
    return answer