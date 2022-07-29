n = int(input())
lst = []
visited = [[ 0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    lst.append(list(input()))
num=1

for x in range(n):
    for y in range(n):
        # 출발 위치 찾기
        if lst[x][y] =='1' and visited[x][y]==0:
            visited[x][y] = num
            queue = [(x, y)]
            # 미로탐색 활용
            while queue:
                i, j = queue.pop(0)
                if i < (n - 1) and lst[i + 1][j] == '1' and visited[i + 1][j] == 0:
                    visited[i + 1][j] = num
                    queue.append((i + 1, j))
                if i > 0 and lst[i - 1][j] == '1' and visited[i - 1][j] == 0:
                    visited[i - 1][j] = num
                    queue.append((i - 1, j))
                if j < (n - 1) and lst[i][j + 1] == '1' and visited[i][j + 1] == 0:
                    visited[i][j + 1] = num
                    queue.append((i, j + 1))
                if j > 0 and lst[i][j - 1] == '1' and visited[i][j - 1] == 0:
                    visited[i][j - 1] = num
                    queue.append((i, j - 1))
            num += 1

max_ = max(map(max, visited)) # 이차원리스트 최대값 찾기
cnt = [0 for i in range(max_)]
print(max_)

for i in visited:
    for j in i:
        if j != 0:
            cnt[j-1] += 1

cnt.sort()
for i in cnt:
    print(i)