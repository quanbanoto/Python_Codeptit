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
a =[[]]*n
for i in range(n):
    a[i] = list(map(int, input().split()))

M = 0
for i in range(n):
    for j in range(m):
        if is_prime(a[i][j]):
            M = max(a[i][j], M)
if M == 0:
    print("NOT FOUND")
else:
    print(M)
    for i in range(n):
        for j in range(m):
            if a[i][j] == M:
                print(f"Vi tri [{i}][{j}]")
# 6 4
# 23 21 26 10
# 13 13 22 14
# 28 29 28 23
# 29 19 11 19
# 16 26 24 21
# 13 25 21 29

