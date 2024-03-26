import math



n, k = map(int, input().split())

x = 10**(k-1)
k = 10**k
cnt = 0
for i in range(x, k):
    if math.gcd(n, i) == 1:
        print(i, end=" ")
        cnt += 1
        if cnt % 10 == 0:
            print()

