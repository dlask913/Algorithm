while True:
    try:
        n = int(input())
    except:
        break
    tmp = 0
    for i in range(1,n+1):
        tmp = tmp*10+1
        tmp %= n
        if tmp == 0:
            print(i)
            break