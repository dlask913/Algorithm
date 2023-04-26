t = int(input())
ans = []

for _ in range(t):
    num = int(input())
    cnt = 0
    i = 5
    while i<=num:
        cnt += num//i
        i*=5
    print(cnt)
