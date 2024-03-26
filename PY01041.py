def so_tang_giam(n):
    l = len(n)
    if l < 3:
        return "NO"
    i = 0
    while i < l - 1 and n[i] < n[i + 1]:
        i += 1
    if n[i] == n[i - 1]:
        return "NO"
    while i < l - 1 and n[i] > n[i + 1]:
        i += 1
    if i != l - 1:
        return "NO"
    return "YES"


for i in range(int(input())):
    print(so_tang_giam(input()))