import math


def nguyen_to_cung_nhau(a, b, c):
    if 1 == math.gcd(a, b) == math.gcd(b, c) == math.gcd(c, a):
        return 1
    return 0


l, r = map(int, input().split())
for i in range(l, r - 1):
    for j in range(i +  1, r):
        for k in range(j + 1, r + 1):
            if nguyen_to_cung_nhau(i, j, k):
                print(f"({i}, {j}, {k})")