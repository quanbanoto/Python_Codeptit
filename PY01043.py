def thuan_nghich_chan(n):
    n = str(n)
    if n != n[::-1]:
        return 0
    if len(n) % 2 != 0:
        return 0
    for i in n:
        if int(i) % 2 != 0:
            return 0
    return 1


s = []


for i in range(22, 888890, 2):
    if thuan_nghich_chan(i):
        s.append(i)
for i in range(int(input())):
    n = int(input())
    for j in s:
        if j < n:
            print(j, end=" ")
        else:
            break
    print()
