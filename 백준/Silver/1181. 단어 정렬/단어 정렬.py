import sys
n=int(sys.stdin.readline())
word=[]
for i in range(n):
    word.append(sys.stdin.readline().strip())

word.sort()
word.sort(key=len)

word = list(dict.fromkeys(word))

for i in word:
    print(i)