def thuan_nghich(n):
    s = 0
    for i in n:
        s += int(i)
    s1 = str(s)
    if s1[::-1] == s1 and s > 10:
        return "YES"
    return "NO"


for i in range(int(input())):
    print(thuan_nghich(input()))