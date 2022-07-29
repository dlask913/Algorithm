n,m=map(int,input().split())
lst=[]
for i in range(n):
    lst.append(list(input()))

queue=[(0,0)] # 좌표 저장 공간
visited = [[ 0 for _ in range(m)] for _ in range(n)] # 방문 여부 및 경로 갱신
visited[0][0]=1
i = 0
j = 0

while queue:   
    i,j = queue.pop(0)
    
    if i == (n-1) and j == (m-1):
        break

    if i < (n-1) and visited[i+1][j]==0 and lst[i + 1][j] == '1':
        visited[i + 1][j] = visited[i][j] + 1
        queue.append((i+1,j))

    if j < (m-1) and visited[i][j+1]==0 and lst[i][j+1] == '1':
        visited[i][j+1] = visited[i][j] + 1
        queue.append((i,j+1))

    if i > 0 and visited[i-1][j]==0 and lst[i-1][j] == '1':
        visited[i-1][j] = visited[i][j]+1
        queue.append((i-1,j))

    if j>0 and visited[i][j-1]==0 and lst[i][j-1] == '1':
        visited[i][j-1] = visited[i][j]+1
        queue.append((i,j-1))

print(visited[n-1][m-1])