x = input()
p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while x != "0":
    [k, s] = x.split()
    k = int(k)
    s = list(s)
    l = len(s)
    for i in range(l):
        s[i] = p[(p.find(s[i]) + k)%28]
    print(''.join(s[::-1]))
    x = input()
