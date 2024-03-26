def thang_bang(n):
    m = n[::-1]
    l = len(n)
    for i in range(l - 1, 0, -1):
        if abs(ord(n[i]) - ord(n[i-1])) != abs(ord(m[i]) - ord(m[i-1])):
            return "NO"
    return "YES"

for i in range(int(int(input()))):
    print(thang_bang(input()))