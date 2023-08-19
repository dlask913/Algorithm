from heapq import heappop,heappush
n = int(input())
card = []
for _ in range(n):
    heappush(card,int(input()))
card.sort()
s = 0
while card:
    if len(card) == 1:
        print(s)
        break
    a = heappop(card)
    b = heappop(card)
    s += (a+b)
    heappush(card, a+b)
