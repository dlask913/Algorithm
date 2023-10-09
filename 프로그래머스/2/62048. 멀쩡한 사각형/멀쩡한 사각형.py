""" gcd ( 입출력 예 #1 )
1. 규칙적인 빈 칸들이 최대공약수(4)만큼 반복되는 것을 그래프를 통해 확인
2-1. 총 가로 길이 8을 최대공약수로 나눈 값인, 2
2-2. 총 세로 길이 12를 최대공약수로 나눈 값인, 3
3. 그럼 2*3 직사각형에서 가로 2칸과 세로 3칸은 꼭 지나야하는데 값이 중복되기 때문에 -1
 ex> 2 + 3 - 1 = 4 
4. 규칙적인 빈 칸의 수를 구했으므로, 최대공약수만큼 곱해서 총 빈 칸 개수 구학.
 ex> 4 * 4 = 16 
"""
def gcd(m,n): # 시간 초과 때문에 유클리드 호제법 사용
    while n != 0:
        m,n = n,m%n
    return abs(m)

def solution(w,h):
    res = gcd(w,h)
    answer = w*h - res * (w//res + h//res - 1)
    return answer