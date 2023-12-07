""" 유클리드호제 """
def gcd(a,b): # 최대공약수
    if b == 0: return a
    return gcd(b,a%b)

def lcm(a,b): # 최소공배수
    return (a*b) // gcd(b,a%b)

def solution(arr):
    n = len(arr)
    
    ans = 1
    for i in range(n): # N 개의 최소 공배수 구하기
        ans = lcm(ans,arr[i])
        
    return ans