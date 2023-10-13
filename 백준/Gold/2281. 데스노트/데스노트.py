n, m = map(int, input().split())
name = []
res = float("inf")
memo = {} # 메모이제이션을 위한 딕셔너리 생성
def write(idx,cur,prev):
    global res
    if idx == n:
        res = min(res, prev)
        return
    if prev >= res:
        return

    if (idx, cur) in memo and memo[(idx, cur)] <= prev:
        return

    # 현재 줄에 쓸건지
    if (cur + name[idx] + 1) <= m:
        write(idx+1,cur+name[idx]+1,prev)
    # 다음 줄에 쓸건지
    write(idx+1,name[idx],prev+(m-cur)**2)

    memo[(idx, cur)] = prev

for _ in range(n):
    name.append(int(input()))

write(1,name[0],0)
print(res)