a, k, n = input().split()
a, k, n = int(a), int(k), int(n)
x = n - a
cnt = 0
j = k - a % k

while j <= x:
    print(j, end=" ")
    cnt = 1
    j += k

if cnt == 0:
    print(-1)