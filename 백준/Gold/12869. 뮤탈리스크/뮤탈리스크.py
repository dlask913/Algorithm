n = int(input())
hp = list(map(int,input().split()))
cnt = 0
ans = []
attack = [[9,3,1],[9,1,3],[3,9,1],[3,1,9],[1,9,3],[1,3,9]]
dp = [[[-1 for _ in range(60)] for _ in range(60)] for _ in range(60)]

for _ in range(3-n):
    hp += [0]
def search(x,y,z,cnt):
    x = 0 if x <= 0 else x
    y = 0 if y <= 0 else y
    z = 0 if z <= 0 else z
    if x <= 0 and y <= 0 and z <= 0:
        ans.append(cnt)
        return

    if dp[x][y][z] > cnt or dp[x][y][z] == -1: # 한 번도 방문 안했거나 현재 cnt 가 더 작을 때
        dp[x][y][z] = cnt
    else: return

    for i in attack:
        cnt += 1
        search(x - i[0], y - i[1], z - i[2], cnt)
        cnt -= 1

for i in attack:
    search(hp[0]-i[0],hp[1]-i[1],hp[2]-i[2],0)

print(min(ans)+1)