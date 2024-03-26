def tong_tich(n):
    tong = 0
    l = len(n)
    le = 0
    tich = 1
    for i in range(0, l, 2):
        tong += int(n[i])
    for i in range(1, l, 2):
        if int(n[i]) == 0:
            le += 1
        else:
            tich *= int(n[i])
    if le == int(l / 2):
        tich =  0
    return f"{tong} {tich}"

for i in range(int(input())):
    print(tong_tich(input()))
