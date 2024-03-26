import math


def is_prime(n):
    if n < 2:
        return "NO"
    x = int(math.sqrt(n)) + 1
    for i in range(2, x):
        if n % i == 0:
            return "NO"
    return "YES"


for i in range(int(input())):
    print(is_prime(int(input()[-4:])))
