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

for i in range(int(input())):
    n = input()
    if is_prime(int(n[0:3])) and is_prime(int(n[-3:])):
        print("YES")
    else:
        print("NO")
