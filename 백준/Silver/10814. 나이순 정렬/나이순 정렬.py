n = int(input())
lst=[]
for i in range(n):
    a,b=input().split()
    lst.append([int(a),b,i])
lst.sort(key=lambda x:(x[0],x[2]))
for i,j,k in lst:
    print(i,j)