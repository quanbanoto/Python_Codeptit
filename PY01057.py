import math


def is_prime(n):
    if n == 2 or n == 3 or n == 5 or n == 7:
        return 1
    if n < 2:
        return 0
    x = int(math.sqrt(n)) + 1
    for i in range (2, x):
        if n % i == 0:
            return 0
    return 1


def check(n):
    l = len(n)
    for i in range(l):
        if (is_prime(i) == 1 and is_prime(int(n[i])) == 0) or(is_prime(i) == 0 and is_prime(int(n[i])) == 1):
            return "NO"
    return "YES"


for i in range(int(input())):
    print(check(input()))
