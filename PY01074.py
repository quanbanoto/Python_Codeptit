a = []


def sang():
    a.append(0)
    a.append(0)
    a.append(1)
    for i in range(2, 2000000):
        a.append(1)
    x = int(2000000 ** 0.5)
    for i in range(2, x):
        if a[i] == 1:
            for j in range(i * i, 2000000, i):
                a[j] = 0
    return

def tong_uoc_so(n):
    if a[n] == 1:
        return n
    tong = 0
    i = 2
    x = int(n**0.5) + 1
    while i < x:
        if n % i == 0:
            while n % i == 0:
                tong += i
                n /= i
        i += 1
    if a[int(n)]:
        tong += n
    return tong


s = 0
sang()
for i in range(int(input())):
    s += tong_uoc_so(int(input()))
print(int(s))
