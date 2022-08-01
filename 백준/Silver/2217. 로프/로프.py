n = int(input())
k=[]
greedy = []
for i in range(n):
    k.append(int(input()))

k.sort(reverse=True)

for i in range(n):
    greedy.append(k[i]*(i+1))

print(max(greedy))