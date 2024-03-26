def thuan_nghich(n: str):
    return len(n) >= 2 and n == n[::-1]

n, m = map(int, input().split())
a = [[]] * n

for i in range(n):
    a[i] = [int(x) for x in input().split()]

M = 0
for i in range(n):
    for j in range(m):
        if thuan_nghich(str(a[i][j])):
            M = max(M, a[i][j])

if M == 0:
    print("NOT FOUND")
else:
    print(M)
    for i in range(n):
        for j in range(m):
            if M == a[i][j]:
                print(f"Vi tri [{i}][{j}]")

# 6 4
# 23 21 77 10
# 13 13 22 14
# 28 29 28 23
# 29 77 11 19
# 16 26 24 21
# 13 25 77 77