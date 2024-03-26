import math


def isPrime(n):
    if(n < 2):
        return "NO"
    s = int(math.sqrt(n))
    for i in range(2, s + 1):
        if n % 2 == 0:
            return "NO"
    return "YES"

for i in range(0, int(input())):
    n = int(input())
    cnt = 0
    for j in range(1, n):
        if math.gcd(n, j) == 1:
            cnt += 1
    print(isPrime(cnt))