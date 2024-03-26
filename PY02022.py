a = [0, 0]
for i in range(2, 1000000):
    a.append(1)
for i in range(2, 1000):
    if a[i] == 1:
        for j in range(i * i, 1000000, i):
            a[j] = 0

n = int(input())
b = list(map(int, input().split()))
myMap = {}

for i in b:
    if i not in myMap:
        if a[i] == 1:
            myMap[i] = 1
    else:
        myMap[i] += 1

for i in b:
    if i in myMap and myMap[i] > 0:
        print(i, myMap[i])
        myMap[i] = 0

