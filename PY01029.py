import math

for i in range(int(input())):
    n = input()
    m = n[::-1]
    n = int(n)
    m = int(m)
    if math.gcd(m, n) == 1:
        print("YES")
    else:
        print("NO")

