s = input()
l = len(s)
s = s[::-1]
res = ''
for i in range(0, l):
    if i % 3 == 0 and i != 0:
        res += ','
    res += s[i]

print(res[::-1])