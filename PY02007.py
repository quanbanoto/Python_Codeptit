s = set({})
a = []
while len(a) < 10:
    b = list(map(int, input().split()))
    a.extend(b)

for i in range(10):
    s.add(a[i] % 42)
print(len(s))
