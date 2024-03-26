def tich_tong(n):
    tong = 0
    l = len(n)
    tich = 1
    for i in range(1, l, 2):
        tong += int(n[i])
    for i in range(0, l, 2):
        if int(n[i]) != 0:
            tich *= int(n[i])
    return f"{tich} {tong}"

for i in range(int(input())):
    print(tich_tong(input()))
