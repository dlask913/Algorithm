from itertools import combinations
from collections import deque

def bfs(virus, n):
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    q = deque(virus)
    v = [[-1 for _ in range(n)] for _ in range(n)]

    for x, y in virus: # 바이러스가 있는 위치 0초
        v[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and lab[nx][ny] != 1 and v[nx][ny] == -1: # 벽이 아니고 방문 아직 안했을 때
                v[nx][ny] = v[x][y] + 1
                q.append((nx, ny))

    for i in range(n):
        for j in range(n):
            if lab[i][j] != 1 and v[i][j] == -1: # 벽이 아닌데 방문 안했을 경우
                return float('inf')

    return max(max(x) for x in v) # v 배열에서의 최대값은 결국 다 퍼지는데 걸린 시간


n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

virus = [(i, j) for i in range(n) for j in range(n) if lab[i][j] == 2] # 바이러스 둘 수 있는 모든 위치 찾기

res = float('inf')
for v in combinations(virus, m): # m 개로 묶은 모든 바이러스 조합
    res = min(res, bfs(v, n))
print(res if res != float('inf') else -1)