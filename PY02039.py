n = int(input())
a = [[]] * n
for i in range(n):
    a[i] = [int(x) for x in input().split()]
k = int(input())
tong_tren = 0
tong_duoi = 0
for i in range(n):
    for j in range(n):
        if i > j: tong_duoi += a[i][j]
        if i < j: tong_tren += a[i][j]
res = abs(tong_duoi - tong_tren) - k
if res <= 0:
    print("YES")
else:
    print("NO")
print(abs(tong_duoi - tong_tren))
