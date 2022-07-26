import sys
n = int(sys.stdin.readline())
job = list()
for i in range(n):
    x,y = map(int,sys.stdin.readline().split())
    job.append([x,y])
job.sort()
job=sorted(job, key=lambda job: job[1])
m = list()
for i in range(len(job)):
    if i == 0:
        m.append(job[i])
    else:
        if m[-1][-1] <= job[i][0]:
            m.append(job[i])
print(len(m))