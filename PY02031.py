import math

def is_prime(n):
    if n < 2:
        return 0
    x = int(math.sqrt(n)) + 1
    for i in range(2, x):
        if n % i == 0:
            return 0
    return 1



n, m = map(int, input().split())
a = [[]] * n
for i in range(n):
    a[i] = [int(x) for x in input().split()]
for i in range(n):
    for j in range(m):
        if is_prime(a[i][j]):
            print(1,  end=" ")
        else:
            print(0, end=" ")
    print()
