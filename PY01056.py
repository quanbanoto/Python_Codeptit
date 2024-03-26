import math


def is_prime(n):
    if n < 2:
        return "NO"
    x = int(math.sqrt(n)) + 1
    for i in range(2, x):
        if n % i == 0:
            return "NO"
    return "YES"


def check(n):
    l = len(n)
    s = 0
    for i in range(l):
        if (i % 2 == 0 and int(n[i]) % 2 != 0) or(i % 2 != 0 and int(n[i]) % 2 == 0):
            return "NO"
        s += int(n[i])
    return is_prime(s)

for i in range(int(input())):
    print(check(input()))

