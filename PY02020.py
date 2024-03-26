n = int(input())
a = list(map(float, input().split()))
m = min(a)
M = max(a)
cnt = 0
res = 0
for i in a:
    if i != m and i != M:
        cnt += 1
        res += i
print("{:.2f}".format(res/cnt))
