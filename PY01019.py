def check(s1, s2):
    i = len(s1) - 1
    while i > 0:
        if abs(ord(s1[i]) - ord(s1[i - 1])) != abs(ord(s2[i]) - ord(s2[i - 1])):
            return "NO"
        i -= 1
    return "YES"


for i in range(int(input())):
    s1 = str(input())
    s2 = s1[::-1]
    print(check(s1, s2))
