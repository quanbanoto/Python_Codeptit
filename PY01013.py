import math


def is_prime(n):
    if n < 2:
        return 0
    can2 = int(math.sqrt(n)) + 1
    for i in range(2, can2):
        if n % i == 0:
            return 0
    return 1


for i in range(int(input())):
    [p, q] = input().split()
    p, q = int(p), int(q)
    x = math.gcd(p, q)
    x = str(x)
    res = 0
    for i in x:
        res += int(i)
    if is_prime(res):
        print("YES")
    else:
        print("NO")
