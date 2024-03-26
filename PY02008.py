is_prime = [0, 0]
for i in range(2, 1000000):
    is_prime.append(1)
for i in range(2, 1000):
    if is_prime[i] == 1:
        for j in range(i * i, 1000000, i):
            is_prime[j] = 0

a = []
for i in range(2, 1000000):
    if is_prime[i] == 1:
        a.append(i)
n, x = map(int, input().split())
b = [x]
for i in range(1, n + 1):
    b.append(a[i - 1] + b[i - 1])
for i in b:
    print(i, end=' ')