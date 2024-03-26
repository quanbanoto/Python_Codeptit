for i in range(0, int(input())):
    [n, m] = input().split()
    n, m = int(n), int(m)
    a = list(map(int, input().split()))
    for i in range(m, n):
        print(a[i], end = ' ')
    for i in range(0, m):
        print(a[i], end = ' ')
    print()