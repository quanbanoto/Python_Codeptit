import math


def is_prime(n):
    if n < 2:
        return 0
    x = int(math.sqrt(n)) + 1
    for i in range(2, x):
        if n%i == 0:
            return 0
    return 1



for i in range(int(input())):
    n = input()
    l = len(n)
    cnt = 0
    if is_prime(l):
        for i in n:
            if is_prime(int(i)):
                cnt += 1
        if cnt > l - cnt:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
