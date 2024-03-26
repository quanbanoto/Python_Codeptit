def lam_tron(n):
    l = len(n)
    if l == 1:
        return n
    res = ""
    x = 0
    i = l - 1
    while i > 0:
        h = int(n[i]) + x
        if h >= 5:
            x = 1
        else:
            x = 0
        res = "0" + res 
        i -= 1
    if x == 1:
        res = str(int(n[i]) + 1) + res
    else:
        res = n[i] + res
    return res

for i in range(0, int(input())):
    print(lam_tron(input()))

# 7
# 15
# 14
# 5
# 99
# 12345678
# 44444445
# 1445