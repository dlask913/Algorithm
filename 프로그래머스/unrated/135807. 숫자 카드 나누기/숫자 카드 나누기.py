def gcd(a, b):
    if a % b == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a % b)

def solution(arrayA, arrayB):
    gcA,gcB = 0,0
    for i in arrayA:
        gcA = gcd(gcA,i)
    
    for i in arrayB:
        gcB = gcd(gcB,i)
    
    for a in arrayA:
        if a%gcB == 0:
            gcB = 0
            break
    for b in arrayB:
        if b%gcA == 0:
            gcA = 0
            break
    return max(gcA,gcB)