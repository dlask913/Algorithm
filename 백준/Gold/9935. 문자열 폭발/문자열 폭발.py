st = input()
fire = input()
l = len(fire)
stack = []

for x in st:
    stack += [x]
    if x == fire[-1] and stack[-l:]==list(fire):
        for _ in range(l):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")