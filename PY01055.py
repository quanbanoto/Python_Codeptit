def xen_ke(n):
    l = len(n)
    if l % 2 == 0:
        return "NO"
    if n[0] == n[1]:
        return "NO"
    for i in range(0, l - 2, 2):
        if n[i] != n[i + 2]:
            return "NO"
    return "YES"

for i in range(int(input())):
    print(xen_ke(input()))

