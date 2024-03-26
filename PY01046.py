def try1(n, a, b, c):
    if n == 1:
        print(a, '->', c)
        return
    try1(n - 1, a, c, b)
    print(a, '->', c)
    try1(n - 1, b, a, c)

n = int(input())
try1(n, 'A', 'B', 'C')
