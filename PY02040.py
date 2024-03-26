n = int(input())
a = [[]] * n
for i in range(n):
    a[i] = [int(x) for x in input().split()]
k = int(input())

tong_tren = 0
tong_duoi = 0

for i in range(n):
    for j in range(n):
        if i + j < n - 1: tong_tren += a[i][j]
        if i + j > n - 1: tong_duoi += a[i][j]

if abs(tong_duoi - tong_tren) <= k:
    print("YES")
else: 
    print("NO")
print(abs(tong_duoi - tong_tren))
