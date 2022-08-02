import sys
N = int(sys.stdin.readline())
truck = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
box = list(map(int,sys.stdin.readline().split()))
if max(box) > max(truck):
    print(-1)
    sys.exit()
truck.sort(reverse=True)
box.sort(reverse=True)
answer = 0
while box:
    for i in range(N):
        tmp = truck[i] 
        for j in range(len(box)):
            if tmp >= box[j]:
                box.pop(j)
                break
    answer += 1
print(answer)