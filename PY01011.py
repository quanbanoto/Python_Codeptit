def niceNumber(temp):
    n = str(temp)
    m = n[::-1]
    if m != n:
        return 0
    l = len(n)
    if l % 2 != 0:
        return 0
    for i in n:
        if int(i) % 2 != 0:
            return 0
    return 1

nN = []

for i in range(20, 1000000):
    if niceNumber(i):
        nN.append(i)

for i in range(int(input())):
    n = int(input())
    for i in nN:
        if i < n:
            print(i, end=" ")
        else:
            break
    print()
