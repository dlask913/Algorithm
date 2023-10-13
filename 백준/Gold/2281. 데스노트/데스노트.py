n, m = map(int, input().split())
name = []
res = float("inf")
memo = {} # 메모이제이션을 위한 딕셔너리 생성
def write(idx,cur,prev): # (name 순서, 현재 줄에 저장된 값, 지난 줄까지의 제곱 최솟값 )
    global res
    if idx == n: # 모든 이름을 다 적었을 때
        res = min(res, prev)
        return
    if prev >= res or (idx, cur) in memo and memo[(idx, cur)] <= prev: # 이미 계산을 했고 그 값이 현재 계산한 최솟값 보다 작으면 ( 그 이후 계산 필요X )
        return

    # 현재 줄에 쓸건지
    if (cur + name[idx] + 1) <= m:
        write(idx+1,cur+name[idx]+1,prev)
    # 다음 줄에 쓸건지
    write(idx+1,name[idx],prev+(m-cur)**2)

    memo[(idx, cur)] = prev # name[idx] 까지 적었을 때, 제곱 최솟값

for _ in range(n):
    name.append(int(input()))

write(1,name[0],0)
print(res)
