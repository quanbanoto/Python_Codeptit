
a = [1,1]

for i in range(2,93):
    a.append(a[i - 1] + a[i - 2])

for i in range(int(input())):
    x, y = map(int, input().split())
    for i in range(x - 1, y ):
        print(a[i], end=" ")