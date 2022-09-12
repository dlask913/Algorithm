def prime_find(num):
    if num==1: return False
    for i in range(2,int(num**(0.5))+1):
        if num%i == 0:
            return False
    return True
    
def solution(n, k):
    prime=[]
    answer = 0
    while n!=0:
        prime.append(n%k)
        n //=k
    prime=''.join(list(map(str,prime)))[::-1]
    
    idx = 0
    for i in prime.split('0'):
        if i and prime_find(int(i)):
            answer += 1
            
    return answer