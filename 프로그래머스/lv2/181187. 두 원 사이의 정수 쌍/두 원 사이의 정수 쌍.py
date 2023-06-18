import math
def solution(r1, r2):
    answer = 0
    x,y=0,0
    edge = 0
    for i in range(1,r1):
        x += math.ceil(math.sqrt(r1**2 - i**2))
        if x%1 == 0: edge += 1
        
    for i in range(1,r2):
        y += math.floor(math.sqrt(r2**2 - i**2))
    answer = (y-x+edge)*4 + (r2-r1)*4 + 4
    return answer

