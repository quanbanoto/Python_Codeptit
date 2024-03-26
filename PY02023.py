import functools


def tong(n):
    s = str(n)
    t = 0
    for i in s:
        t += int(i)
    return t


def cmp(a, b):
    if tong(a) == tong(b):
        if a > b:
            return 1
        else:
            return -1
    elif tong(a) > tong(b):
        return 1
    else:
        return -1


for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a, key=functools.cmp_to_key(cmp))
    for i in a:
        print(i, end=" ")
    print()
# 1
# 8
# 143 43 22 99 7 9 1111 10000000
