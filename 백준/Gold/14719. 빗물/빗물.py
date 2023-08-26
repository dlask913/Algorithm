h,w = map(int,input().split()) # 세로,가로 길이
l = list(map(int,input().split()))
dic = {x:[] for x in range(h+1)} # 각 높이의 위치 담을 공간
cnt = 0
for k, v in enumerate(l):
    for x in range(v+1): # 자기 높이보다 작은 높이에 다 추가
        dic[x].append(k)

for k,v in dic.items():
    if len(v) <= 1:
        continue
    for x in range(v[0], v[-1]): # 가능한 최대 범위
        if l[x] < k:
            cnt += 1
            
print(cnt)