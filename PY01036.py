for i in range(int(input())):
    n = int(input())
    x = 0
    res = 0.0
    if n % 2 == 0:
        x = 2
    else:
        x = 1
    for i in range(x, n + 1, 2):
        res += (1.0 / i)
    print("{:.6f}".format(res))