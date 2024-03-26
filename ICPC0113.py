import math


prime = [0, 0]
for i in range(2, 1000000):
    prime.append(1)
for i in range(2, 1000):
    if prime[i] == 1:
        for j in range(i*i, 1000000, i):
            prime[j] = 0

for i in range(int(input())):
    n = int(input())
    for i in range(13, n):
        x = str(i)[::-1]
        x = int(x)
        if n > x > i and prime[i] == 1 and prime[x] == 1:
            print(i, x, end=' ')
    print()
