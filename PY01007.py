for i in range(0, int(input())):
    [n, x, m] = input().split()
    n, x, m = float(n), float(x), float(m)
    cnt = 0
    while n < m:
        n = n*(1+x/100)
        cnt += 1
    print(cnt)
