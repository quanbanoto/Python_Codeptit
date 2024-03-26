n, m = map(int, input().split())
a = [[]] * n

for i in range(n):
    a[i] = [int(x) for x in input().split()]

if n > m:
    x = (n - m - 1) * 2
    b = []
    for i in range(0, x + 1, 2):
        b.append(i)
    for i in range(n):
        if i not in b:
            for j in range(m):
                print(a[i][j], end=" ")
            print()
else:
    x = (m - n - 1)*2+1
    b = []
    for j in range(1, x + 1, 2):
        b.append(j)
    for i in range(n):
        for j in range(m):
            if j not in b:
                print(a[i][j], end=" ")
        print()

# 6 4
# 2 8 7 6
# 6 3 2 6
# 7 2 2 8
# 9 9 9 8
# 9 6 6 3
# 7 7 4 9
        
# 4 6
# 2 8 7 6 4 3
# 6 3 2 6 7 2
# 7 2 2 8 9 1
# 9 9 9 8 0 7