def solution(numbers, hand):
    answer = ''
    loc = {"l":(3,0),"r":(3,2)} # 현재 위치
    
    for n in numbers:
        if n == 3 or n == 6 or n == 9: # 3,6,9 오른손
            loc["r"] = (n//3-1,2)
            answer += 'R'
        elif n == 1 or n == 4 or n == 7 : # 1,4,7 왼손
            loc["l"] = ((n-1)//3,0)
            answer += 'L'
        else:
            x,y = (n-2)//3 if n!=0 else 3,1
            """ 유클리드 쓰면 X, 맨해튼 거리 계산 O"""
            dr = abs(loc["r"][0]-x) + abs(loc["r"][1]-y)
            dl = abs(loc["l"][0]-x) + abs(loc["l"][1]-y)
            
            if dr == dl: # 길이 같으면 hand 에 따라
                res = "r" if hand == "right" else "l" 
                loc[res] = (x,y)
            else: # 더 가까운 거리
                res = "r" if dr < dl else "l" 
                loc[res] = (x,y)
            answer += res.upper()
            
    return answer