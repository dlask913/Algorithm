n = int(input())
play = []
for _ in range(n):
    play.append(list(map(int,input().split())))

mini = [[0,0,0],[0,0,0]] # 메모리 초과 방지
maxi = [[0,0,0],[0,0,0]]
for i in range(3):
    mini[0][i] = play[0][i]
    maxi[0][i] = play[0][i]

for i in range(1,n):
    mini[1][0] = min(mini[0][0], mini[0][1]) + play[i][0] # 가장 왼 쪽은 바로 아래 / 대각선 아래 오른쪽
    mini[1][1] = min(mini[0][0], mini[0][1], mini[0][2]) + play[i][1] # 중간은 대각선 아래 왼쪽/ 가운데 / 대각선 아래 오른쪽
    mini[1][2] = min(mini[0][1], mini[0][2]) + play[i][2] # 가장 오른 쪽은 바로 아래 / 대각선 아래 왼쪽

    maxi[1][0] = max(maxi[0][0], maxi[0][1]) + play[i][0]
    maxi[1][1] = max(maxi[0][0], maxi[0][1], maxi[0][2]) + play[i][1]
    maxi[1][2] = max(maxi[0][1], maxi[0][2]) + play[i][2]

    for j in range(3): # 값 초기화
        mini[0][j] = mini[1][j]
        maxi[0][j] = maxi[1][j]

print(max(maxi[0]),min(mini[0])) # n=1 인 경우를 대비해 0번째 행의 값 출력
