def solution(brown, yellow):
    answer = []
    q = []
    if yellow==1:
        return [3,3]
    
    for i in range(1,yellow//2+1):
        if yellow%i==0 and i<=(yellow//i):
            q.append((i,yellow//i))
    
    for i,j in q:
        if i*2+j*2+4 == brown:
            answer = [j+2,i+2]
    
    return answer