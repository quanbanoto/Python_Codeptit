def luckyNumber(n):
    for i in n:
        if i != '4' and i != '7':
            return "NO"
    return "YES"

for i in range(0, int(input())):
    print(luckyNumber(input()))
