def dauCuoi(s):
    if s[0:2] == s[-2:]:
        return "YES"
    return "NO"

for i in range(0, int(input())):
    print(dauCuoi(input()))
