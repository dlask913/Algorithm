
# Online Python - IDE, Editor, Compiler, Interpreter
"""
풀어야 할 문제는 입력으로 주어지는 사용할 벽장의 순서에 따라서 벽장문을 이동하는 순서를 찾는 것이다. 이때 벽장문의 이동횟수를 최소로 하여야 한다. 입력은 다음과 같이 주어지며, 열려있는 벽장의 개수는 항상 2개이다.

예를 들어 사용할 벽장 순서가 3 1 6 5이면, 3번 앞의 문을 2번으로 옮겨서 3번 벽장을 사용하고(문 이동횟수=1), 다음에 1번과 2번 앞에 있는 문을 오른쪽으로 하나씩 옮겨서(문 이동횟수=2) 1번 벽장을 사용하며, 6번 앞에 있는 문을 왼쪽으로 옮겨서 6번 벽장을 사용하고(문 이동횟수=1), 다시 그 문을 오른쪽으로 옮겨서 5번 벽장을 사용한다(문 이동횟수=1), 따라서 문이 이동한 횟수의 합은 5이다.

입력
첫 번째 줄에 벽장의 개수를 나타내는 3보다 크고 20보다 작거나 같은 하나의 정수, 두 번째 줄에 초기에 열려있는 두 개의 벽장을 나타내는 두 개의 정수, 그리고 세 번째 줄에는 사용할 벽장들의 순서의 길이(최대 20), 그리고 그 다음줄부터 사용할 벽장의 번호가 한줄에 하나씩 순서대로 주어진다.

출력
벽장문의 최소 이동횟수를 화면에 출력한다.

예제 입력 1 
7
2 5
4
3
1
6
5
"""
n= int(input())
x,y = map(int,input().split())
l = int(input())
seq = []
ans = []

def bruteforce(lev,cost,a,b):
    global ans
    if lev >= l:
        ans.append(cost)
        return
    bruteforce(lev+1, cost+abs(a-seq[lev]),seq[lev],b)
    bruteforce(lev+1, cost+abs(b-seq[lev]),a,seq[lev])
    
for _ in range(l):
    seq.append(int(input()))
    
bruteforce(0,0,x,y)
print(min(ans))