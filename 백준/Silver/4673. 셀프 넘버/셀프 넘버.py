for i in range(1,10001):
    flag = 1
    for j in range(1,i):
        k = j + (j%10) + (j//10%10) + (j//100%10) + (j//1000%10)
        if k == i:
            flag = 0
    if flag:
        print(i)