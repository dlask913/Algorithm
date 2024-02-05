from itertools import combinations
while True:
    n = input()
    if n == "0":
        break
    num = list(map(int,n.split()))
    for i in sorted(combinations(num[1:], 6)):
        print(*i)
    print()
