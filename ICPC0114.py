import math


def prime(n):
    if n <= 1:
        return 0
    x = int(math.sqrt(n)) + 1
    for i in range(2, x):
        if n % i == 0:
            return 0
    return 1

def prime1(n):
    if n == 2 or n == 3 or n == 5 or n == 7:
        return 1
    return 0

def tong(n):
    x = 0
    a = str(n)
    for i in a:
        x += int(i)
    return x


for i in range(int(input())):
    n = int(input())
    x = int(str(n)[::-1])
    if prime1(n) and prime(tong(n)) and prime(n) and prime(x):
        print("Yes")
    else:
        print("No")
