def so_dep(n):
    l = len(n)
    for i in range(0, l - 2):
        if n[i] != n[i + 2] or n[i] == n[i + 1]:
            return "NO"
    return "YES"


for i in range(int(input())):
    print(so_dep(input()))