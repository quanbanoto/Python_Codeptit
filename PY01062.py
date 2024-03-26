import math


def is_prime(n): #n la string
    if n == 2 or n == 3 or n == 5 or n == 7:
        return 1
    if n < 2:
        return 0
    x = int(math.sqrt(n)) + 1
    for i in range (2, x):
        if n % i == 0:
            return 0
    return 1

def check(n): #n la string
    l = len(n)
    if not is_prime(l):
        return "NO"
    not_prime = 0
    for i in n:
        if not is_prime(int(i)):
            not_prime += 1
    if 2 * not_prime >= l:
        return "NO"
    return "YES"




for i in range(int(input())):
    print(check(input()))

