import math


def phan_tich(n):
    y = []
    y.append('1 ')
    x = int(n / 2)
    i = 2
    while i <= x:
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n /= i
            y.append(f"* {i}^{cnt} ")
        i += 1
    if n != 1:
        y.append(f"* {n}^1")
    return y


for i in range(int(input())):
    print(''.join(phan_tich(int(input()))))