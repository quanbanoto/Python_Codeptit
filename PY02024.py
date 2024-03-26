import functools


def tich(n):
    x = str(n)
    s = 1
    for i in x:
        s *= int(i)
    return s


def cmp(a, b) :
    if tich(a) == tich(b) :
        if a > b:
            return 1
        else:
            return -1
    elif tich(a) > tich(b):
        return 1
    else:
        return -1



for t in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    a = sorted(a, key=functools.cmp_to_key(cmp))
    for i in a:
        print(i, end=" ")
    print()
# 1
# 8
# 143 43 22 99 7 9 1111 10000000
