from collections import deque
wheel = []
for _ in range(4):
    wheel.append(list(input()))
k = int(input())
rot = deque()
for _ in range(k):
    a,b = map(int,input().split())
    rot.append((a-1,b))

def rotation(x,lst):
    if x==-1:
        lst = lst[1:] + [lst[0]]
    if x==1:
        lst = [lst[-1]] + lst[:-1]
    return lst

while rot:
    w,d = rot.popleft()
    if w > 0 and wheel[w][6] != wheel[w-1][2]:
        if (w-1) > 0 and wheel[w-1][6] != wheel[w-2][2]:
            if (w-2) > 0 and wheel[w-2][6] != wheel[w-3][2]:
                wheel[w - 3] = rotation(-d, wheel[w - 3])
            wheel[w - 2] = rotation(d, wheel[w - 2])
        wheel[w-1] = rotation(-d, wheel[w - 1])

    if w < 3 and wheel[w][2] != wheel[w+1][6]:
        if (w+1) < 3 and wheel[w+1][2] != wheel[w + 2][6]:
            if (w + 2) < 3 and wheel[w + 2][2] != wheel[w + 3][6]:
                wheel[w + 3] = rotation(-d, wheel[w + 3])
            wheel[w + 2] = rotation(d, wheel[w + 2])
        wheel[w+1] = rotation(-d,wheel[w+1])

    wheel[w] = rotation(d, wheel[w])

ans = 0
for i in range(4):
    if wheel[i][0] == '1':
        ans += (2**i)
print(ans)