def findZero(num):
    idx = -1
    for i in range(len(num)):
        if num[i]=='0':
            idx = i
    return idx
            
def solution(numbers):
    answer = []
    for x in numbers:
        if x%2==0: 
            answer.append(x+1)
        else:
            n = format(x,'b')
            if '0' not in n:
                sol = x + 2**len(n) - 2**(len(n)-1)
            else:
                idx = len(n)-findZero(n)-1
                sol = x + 2**idx - 2**(idx-1)
            answer.append(sol)
            
    return answer