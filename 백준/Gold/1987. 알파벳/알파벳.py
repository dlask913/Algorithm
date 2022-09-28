import sys

r,c = map(int,sys.stdin.readline().split())
alpha = []
visited = [0 for _ in range(26)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
max_= 1


for _ in range(r):
    alpha.append(list(sys.stdin.readline()))

def dfs(x,y,visited,cnt):
    global max_
    max_ = max_ if cnt < max_ else cnt

    if 0<=(x+0)<r and 0<=(y+1)<c and visited[ord(alpha[x+0][y+1])-65]==0:
        visited[ord(alpha[x+0][y+1])-65] = 1
        dfs(x+0,y+1,visited,cnt+1)
        visited[ord(alpha[x+0][y+1])-65] = 0
    if 0 <= (x + 0) < r and 0 <= (y - 1) < c and visited[ord(alpha[x + 0][y - 1]) - 65] == 0:
        visited[ord(alpha[x + 0][y - 1]) - 65] = 1
        dfs(x + 0, y -1, visited, cnt + 1)
        visited[ord(alpha[x + 0][y - 1]) - 65] = 0
    if 0<=(x+1)<r and 0<=(y+0)<c and visited[ord(alpha[x+1][y+0])-65]==0:
        visited[ord(alpha[x+1][y+0])-65] = 1
        dfs(x+1,y+0,visited,cnt+1)
        visited[ord(alpha[x+1][y+0])-65] = 0
    if 0<=(x-1)<r and 0<=(y+0)<c and visited[ord(alpha[x-1][y+0])-65]==0:
        visited[ord(alpha[x-1][y+0])-65] = 1
        dfs(x-1,y+0,visited,cnt+1)
        visited[ord(alpha[x-1][y+0])-65] = 0

visited[ord(alpha[0][0])-65]=1
dfs(0,0,visited,1)

print(max_)
