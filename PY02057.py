import mediapipe
n, m = map(int, input().split())
a =  [[]] * n
mi = 10001
Ma = -1
for i in range(n):
    a[i] = list(map(int, input().split()))
    mi = min(min(a[i]), mi)
    Ma = max(max(a[i]), Ma)
x = Ma - mi
cnt = 1
for i in range(n):
    for j in range(m):
        if a[i][j] == x:
            if cnt ==  1:
                print(x)
                cnt = 0
            print(f"Vi tri [{i}][{j}]")

if cnt == 1:
    print("NOT FOUND")

# 6 4
# 23 21 77 10
# 13 13 22 14
# 28 67 28 23
# 29 77 11 67
# 16 51 24 21
# 13 25 77 77