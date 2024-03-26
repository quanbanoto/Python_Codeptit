n = int(input())
a = [[]] * n
for i in range(n):
    a[i] = [int(x) for x in input().split()]
k = int(input())
tong_duoi= tong_tren=0
for i in range(n):
    for j in range(n):
        if i + j < n - 1: tong_tren += a[i][j]
        elif i + j > n - 1: tong_duoi += a[i][j]

res = abs(tong_duoi - tong_tren) 
if res - k <= 0:
    print("YES")
else:
    print("NO")
print(res)